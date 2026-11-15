import pathlib,json,csv,hashlib,collections,decimal,re
from html.parser import HTMLParser
P=pathlib.Path(__file__).resolve().parent; R=P.parent;decimal.getcontext().prec=80
A='0xd5fbda4c79f38920159fe5f22df9655fde292d47';S1='0x0067cc2416f792cf0ec5629f5506324ac508f859';S2='0x580450dff316ae00d0fbef9621a304020a046ce2';B='0xe5686aae44d392aa6a0637fd38393859502f8667';E1='0x4b304741599c125a244e498d14562487d7109ab8'
def path(g,f):return R/('gamdom-incident-2026-10'+('-'+g if g else ''))/f
def load(g,f):return json.loads(path(g,f).read_text())
def dump(f,d): (P/f).write_text(json.dumps(d,indent=2)+'\n')
def md(f,s):(P/f).write_text(s.strip()+'\n')
refs={}
def ref(g,f):
 p=path(g,f);k=str(p.relative_to(R.parent));refs[k]=hashlib.sha256(p.read_bytes()).hexdigest();return k
rows=[]
for x in load('g010','incident_origin_ledger.json'):
 if x['classification']=='candidate_original_principal':
  y={k:x.get(k) for k in ['chain_id','transaction_hash','block','transaction_index','timestamp_utc','initiator','log_index','token_contract','token_symbol','decimals','token_sender','token_recipient','raw_amount','amount','source_url']};y['provenance']=ref('g010','incident_origin_ledger.json');rows.append(y)
for x in load('g011','upstream_funding_ledger.json'):
 if x['role']=='B_funding':
  y={k:x.get(k) for k in ['chain_id','transaction_hash','block','transaction_index','timestamp_utc','log_index','token_contract','decimals','token_sender','token_recipient','raw_amount','amount','source_url']};y.update(initiator=x['transaction_initiator'],token_symbol=x['symbol'],provenance=ref('g011','upstream_funding_ledger.json'));rows.append(y)
for g,f in [('', 'transaction_ledger.csv'),('g006','historical_transfer_ledger.csv')]:
 for x in csv.DictReader(path(g,f).open()):
  if (not g and x['record_id'] in ['G005-T01','G005-T02']) or (g and x['record_id']=='G006-E009'):
   y=dict(chain_id=137 if not g else 1,transaction_hash=x['tx_hash'],block=int(x.get('block_height') or x['block_number']),timestamp_utc=x['utc_timestamp'],initiator=x['tx_sender'].lower(),log_index=int(x['log_index']) if x.get('log_index') else None,token_contract=x['token_contract'].lower(),token_symbol=x.get('asset') or 'BUSD',decimals=int(x['decimals']),token_sender=x['token_sender'].lower(),token_recipient=x['token_recipient'].lower(),raw_amount=x['raw_amount'],amount=x.get('amount') or x['displayed_amount'],source_url=x['verification_url'],provenance=ref(g,f),verification_basis='Frozen explorer receipt; not newly retrieved RPC');rows.append(y)
rows.sort(key=lambda x:(x['timestamp_utc'],x['chain_id'],x['transaction_hash'],x.get('log_index') or -1))
for i,x in enumerate(rows): x.update(record_id=f'G015-P{i+1:02}',movement_status='CONFIRMED in cited frozen checkpoint',organizational_ownership='UNRESOLVED',unauthorized_status='UNRESOLVED',accounting='Candidate original source outflow within selected coverage; not verified loss')
dump('original_principal_ledger.json',rows)
tot=collections.defaultdict(int)
for x in rows:tot[(x['chain_id'],x['token_contract'] or 'native',x['token_symbol'],x['decimals'])]+=int(x['raw_amount'])
summary=[dict(chain_id=k[0],contract=k[1],symbol=k[2],decimals=k[3],raw_amount=str(v),amount=format(decimal.Decimal(v)/(10**k[3]),'f')) for k,v in sorted(tot.items())];dump('principal_totals.json',summary)
base=load('g010','baseline_comparison.json');tests=[]
for b in base:
 matches=[x for x in rows if x['chain_id']==1 and x['token_sender']==b['address'] and x['token_contract']==b['contract']]
 m=max([int(x['raw_amount']) for x in matches],default=0);n=int(b['maximum_outgoing_raw'] or 0)
 tests.append(dict(**b,incident_selected_outgoing_events=len(matches),incident_max_raw=str(m),maximum_exceeds_bounded_baseline=m>n if n else None,maximum_ratio=str(decimal.Decimal(m)/n) if n else None,test='Compare largest individual canonical event with earlier returned maximum; no distributional anomaly score; no consent inference'))
dump('historical_behavior_baseline.json',dict(ethereum=tests,bnb_S1=load('g011','source_behavior.json'),bnb_incident_max_raw=max(int(x['raw_amount']) for x in rows if x['chain_id']==56 and x['token_sender']==S1),limits='BNB comparator overlaps reported incident window by several minutes; cannot be called wholly pre-incident. Ethereum 26177200–26184449 is Oct12 15:10:35 to Oct13 15:24:35. No complete native/approval/contract baseline or lifetime history. Zero sampled canonical events is insufficient for an anomaly test.'))
ref('g010','baseline_comparison.json');ref('g011','source_behavior.json')
sigs=load('g011','signature_verification.json');orders=load('g012','settlement_order_register.json')
dump('authorization_control_register.json',dict(reused_signature_results=sigs,ethereum_B_authorization=load('g008','evidence/authorization_verification.json'),bnb_approvals=load('g011','approval_register.json'),bnb_orders=[{k:o.get(k) for k in ['order_uid','chain_id','owner','signing_scheme','recovered_eip712_signer']} for o in orders],limits='All results reused, not new signature verification. Distinct A/S1/B public keys do not establish common controller. S2 initiator evidence from G010 receipts is not an independently recovered public-key result in this audit. Permission-path changes for B do not establish how A/S1/S2 instructions were authorized. No exhaustive source-wallet approvals/delegations or historical code scan.'))
for g,f in [('g011','signature_verification.json'),('g008','evidence/authorization_verification.json'),('g011','approval_register.json'),('g012','settlement_order_register.json')]:ref(g,f)
class Text(HTMLParser):
 def __init__(self):super().__init__();self.skip=0;self.out=[]
 def handle_starttag(self,t,a):
  if t in ['script','style']:self.skip+=1
 def handle_endtag(self,t):
  if t in ['script','style']:self.skip=max(self.skip-1,0)
 def handle_data(self,d):
  if not self.skip:self.out.append(d)
sources=[];scan=[]
for f in sorted((P/'evidence').glob('*.json')):
 d=json.loads(f.read_text());p=Text();p.feed(d.get('raw_response_text',''));s=' '.join(p.out)
 sources.append(dict(publication_or_modification_metadata=re.findall(r'(?:dateModified|datePublished)[^,}]{0,100}',d.get('raw_response_text',''))[:5], publication_metadata_limits='Embedded dates may belong to quoted posts; exact official/founder publication times reuse G005, not arbitrary HTML date fields.',id=f.stem,url=d['url'],collected_at=d['requested_at_utc'],http_status=d.get('http_status'),error=d.get('error'),saved_file=str(f.relative_to(P)),authentication='Public HTTPS response from named domain; not signed archive or independent forensic authentication',role='Third-party attribution' if f.stem in ['external_loss_estimate','third_party_wallet_inventory'] else 'Official/archival public documentary source',limitations='Current retrieval alone does not establish pre-incident content; HTML can include quoted posts, navigation and replies. No wallet ownership inferred from labels.'))
 scan.append(dict(source=f.stem,http_status=d.get('http_status'),target_full_address_occurrences={name:len(re.findall(addr,re.sub(r'\s','',s),re.I)) for name,addr in [('A',A),('S1',S1),('S2',S2)]},scan_scope='Rendered textual content excluding scripts/styles; not images, video or account-only content'))
dump('source_register.json',dict(new_acquisitions=sources,frozen_inputs=refs));dump('ownership_evidence_register.json',dict(ownership_claims=[dict(address=a,alias=n,direct_authenticated_attribution='Not found within recorded coverage',third_party_labels='Present in explorer/inventory leads; not ownership proof',organizational_ownership='UNRESOLVED',authorization='UNRESOLVED') for n,a in [('A',A),('S1',S1),('S2',S2)]],text_scans=scan,context='Gamdom public help describes account Wallet Page deposit instructions and changeable addresses. It does not publicly identify these three wallets. Archived deposit guide is assessed only if its response was retrieved.'))
timeline=[dict(timestamp_utc=x['timestamp_utc'],kind='verified source movement',reference=x['record_id'],transaction_hash=x['transaction_hash'],interpretation='Authorization unresolved') for x in rows]
timeline.extend([dict(timestamp_utc='2026-10-14T03:36:58Z',kind='official statement publication',reference='G005 S06; newly archived HTML',claim='Automation-server unauthorized connection and precautionary shutdown; user funds claimed safe',event_time='Detection described approximately 24h earlier; exact access and shutdown times not established'),dict(timestamp_utc='2026-10-14T16:43:53Z',kind='founder statement publication',reference='G005 S07; newly archived HTML',claim='Hot-wallet breach, just over $3m claimed loss, other funds relocated to cold wallets',event_time='No exact movement hashes or precise protective-relocation time identified')]);dump('incident_timeline.json',sorted(timeline,key=lambda x:x['timestamp_utc']))
md('README.md','''# G015 — Ownership, authorization and original-principal audit

Starting checkpoint: f45b9e89053515083e54488a3f925cbc2e44782a. Documentary collection: 16 October 2026 UTC.

This checkpoint consolidates 34 previously verified source movements into one deduplicated principal register, tests bounded historical maxima, and archives primary company statements and public deposit documentation. **Zero newly verified blockchain transactions.** It adds derived accounting and attribution analysis, not a new incident-ownership claim.

A, S1 and S2 organizational ownership and unauthorized status remain UNRESOLVED. Technical transfers and selected signing results are independently verified in the cited frozen checkpoints. No defensible USD unauthorized-loss total is established. An unestablished loss is not a verified zero loss.

Read loss_reconciliation.md, wallet_attribution_matrix.md and coverage_report.md. Run `python verify.py` offline from this directory, within the repository containing the cited frozen checkpoints. `derive.py` regenerates JSON analytical outputs from preserved inputs; `collect.py` acquires public documents without account interaction. Frozen evidence remains unchanged. Medium and X HOLD.
''')
md('wallet_attribution_matrix.md',f'''# Claim-specific attribution matrix

| Wallet | Technical role | Organizational attribution | Key/control evidence | Authorization status |
|---|---|---|---|---|
| A `{A}` | CONFIRMED source to E1 and B, Ethereum/BNB/Polygon | UNRESOLVED: explorer labels are third-party assertions | CONFIRMED selected A signatures and same A key across Ethereum/BNB; no source-wide permission history | UNRESOLVED |
| S1 `{S1}` | CONFIRMED Ethereum E1 and BNB B source | UNRESOLVED: labels/inventory do not authenticate Gamdom control | CONFIRMED selected direct signatures, same S1 key Ethereum/BNB; different key from A | UNRESOLVED |
| S2 `{S2}` | CONFIRMED Ethereum E1 source | UNRESOLVED | CONFIRMED receipt transaction initiator; independent signature recovery NOT ASSESSED here | UNRESOLVED |
| E1 `{E1}` | CONFIRMED receiving/converting account | UNRESOLVED | Transaction initiators preserved in G010; human operator UNRESOLVED | UNRESOLVED |
| B `{B}` | CONFIRMED recipient and settlement/order owner | UNRESOLVED | CONFIRMED selected signatures, Ethereum/BNB EIP-7702 authorizations; first BNB order presigned, second EIP-712 | UNRESOLVED |

## Historical comparison

S1 Ethereum baseline: 308 canonical USDT outflows to 217 recipients, maximum 300251.911353 USDT; 268 USDC outflows to 158 recipients, maximum 1800000 USDC. No prior E1 payments in that returned token sample. G015 compares selected incident maxima in historical_behavior_baseline.json. The incident USDT and USDC individual maxima do not exceed these earlier maxima. This defeats a size-only abnormality claim within this bounded comparison; it does not prove normal intent. Frequency distributions, gas funding and organizational withdrawal purpose were not independently established.

S1 BNB earlier intraday canonical sample: 63 outflows, 49 recipients, maximum 30039.043168179440000000 USDT. The 315446.159624488300000000 payment exceeds that sample maximum. The comparison extends to 15:52:48 and overlaps the reported window; it is not a wholly pre-incident baseline or proof of theft. A and S2 have no comparable canonical outflows in the selected Ethereum baseline, so a meaningful value anomaly test is unavailable. Account nonces establish activity, not ownership or historical business purpose.

## Permission interpretation

B changed execution permissions during the incident window. Ethereum authorization chain 1/nonce 1, outer nonce 0; BNB authorization chain 56/nonce 4, outer nonce 3. Both designate 0x63c0c19a282a1b52b07dd5a65b58948a07dae32b. G008 Ethereum code application was initially explorer-supported; G011 BNB historical code transition was directly read. Preserve those distinctions. Outer key, delegated implementation, solver initiator, order owner and human operator are separate roles. No attributable human signing authority or consent is established. B's new approvals do not retroactively explain source-wallet employee permissions.
''')
md('loss_reconciliation.md','''# Original-principal reconciliation

The ledger selects only G010 `candidate_original_principal`, G011 `B_funding`, G005 T01/T02 and G006 E009. It is a bounded lower coverage of verified movements, not a minimum theft calculation. All quantities are exact integers by chain and contract in principal_totals.json. Thirty-four records are unique; downstream executions are excluded. No token is assumed worth one dollar.

| Chain | Asset | Gross selected source movement |
|---|---|---:|
| Ethereum | USDT | 426040.814198 |
| Ethereum | USDC | 503001.390869 |
| Ethereum | USD1 | 20077.942698961878000000 |
| Ethereum | DAI | 738.148858772417648963 |
| Ethereum | ETH | 86.956356111770671236 |
| Ethereum | BUSD | 10456.137361559383267328 |
| BNB | USDT | 714187.786405077034199428 |
| Polygon | USDT0 | 19610.310097 |
| Polygon | USDC | 12139.456905 |

BNB original source funding 714187.786405077034199428 USDT equals two later Relay deposits 706943.421822265793499428 plus two later settlement debits 7244.364582811240700000. Adding either component to original funding would count the same principal twice. Later Ethereum DAI receipts are consideration/subsequent movement, not additional source loss. G014's last OMFT edge remains SUPPORTED.

G010 separately records E1 returning 0.01 ETH to A. Keep this as a returned movement, not proof of recovery by a company. Source gas and downstream fees are separate from principal. Failed native attempts are excluded. BUSD swaps and Polygon bridge outputs are excluded from new principal. Fungible balances cannot exclusively identify later spending.

The founder's statement claims just over $3m without a public wallet-by-wallet accounting. The external estimate is approximately $4.208m: $2.2m EVM + $965k Solana + $668k Bitcoin + $375k TRON. That arithmetic is reproducible; the valuation and authorization are not independently audited. The estimates may have different chain coverage, gross/net definitions, protective movements, pricing or recoveries. None is resolved by these records. No exact difference from an imprecise 'over $3m' can be calculated.

No timestamped market price series is acquired in G015; no USD conversion or consolidated token-unit total is presented. Solana, Bitcoin, TRON, XRP, Arbitrum and Optimism original-principal coverage is not completed here. Ownership and instruction consent are also unresolved. Consequently independently verified unauthorized loss is **not established**, rather than $0. Customer custodial liabilities and insolvency are not assessed by these asset movements.
''')
md('hypothesis_comparison.md','''# Competing explanations

| Hypothesis | Consistent evidence | Contrary or limiting evidence | Required discriminator |
|---|---|---|---|
| H1 unauthorized extraction | Authenticated company/founder public statements report a breach and loss; clustered transfers to E1/B and later conversions | Statements identify no audited source addresses or exact unauthorized instruction; S1 previously made larger Ethereum transfers; key signatures do not identify an intruder | Authenticated address-specific custody and unauthorized instruction evidence |
| H2 treasury/settlement | Successful direct transfers, valid signing keys, existing S1 high-volume activity, ordinary approvals and protocols | Incident concentration and reported breach require explanation; financial connection does not establish business purpose | Dated authenticated settlement/treasury instructions tied to exact transaction hashes |
| H3 protective relocation | Founder says other hot-wallet funds moved to cold wallets | No transaction-specific cold-wallet declaration or signed protection instruction; conversions alone neither support nor exclude protection | Authenticated cold-storage destination and relocation instructions/timeline |

All three remain UNRESOLVED for specific audited movements. The public breach statement supports occurrence of a reported technical compromise, not unauthorized status of every financially associated transfer. No observation proves a human identity, company ownership or consent. No company claim is independently refuted merely because its disclosed accounting is incomplete.
''')
md('evidence_gap_matrix.md','''# Evidence gaps and stopping boundaries

1. A/S1/S2: no authenticated pre-incident public full-address declaration, custody attestation or publicly verifiable official customer transaction record was obtained. Labels and a third-party wallet inventory cannot fill the gap.
2. Effective signing: selected A/S1/B key use is known; source key custody, employee permissions and source-wide approval/delegation history are not. Valid transactions do not resolve legitimate consent.
3. Historical behavior: short canonical-token windows, not complete source-wallet operations, native history or matched business-day samples. No formal anomaly score or daily rate extrapolation is justified.
4. Timing: official publication times are known from G005; claimed detection is approximate. Exact discovery, shutdown and protective-action timestamps remain unavailable.
5. Loss: original-source selection is bounded; missing networks, historical prices, custody ownership, refunds and protective classifications prevent a defensible USD loss.
6. Customer funds: public safety assurance is a company claim; reserve/liability audit, dated complete withdrawal functionality and reimbursement coverage are not established.

Stop ownership branches at these documentary boundaries. Do not expand secondary wallets or reopen OMFT proof work. Highest-value next independent lead: a pre-13 October public web-archive snapshot containing an official full-address withdrawal/deposit record or custody declaration matching A/S1/S2 and a transaction hash. Such a record would address organizational attribution; it would still not prove lack of consent.
''')
md('coverage_report.md','''# Coverage and source independence

G015 reuses frozen G005/G006/G008/G009/G010/G011/G012/G013/G014 findings without re-verifying their blockchain transactions. The newly derived principal register has 34 movements; no new blockchain transaction is counted. The full prior 266 tracked frozen files are preserved by parent-tree comparison, not by editing their reports.

New public GET acquisition archive includes official Help Center deposit/channel/withdrawal pages, official public home, company/founder X statements, external investigator estimate, Wayback CDX and selected deposit-guide replay, and third-party DappRadar inventory. Each actual response is recorded; a response code is not equivalent to usable content. Official pages and official account statements are primary for their own claims, not independent forensic proof of those claims. The archive is a documentary copy, not a signed WARC or cryptographic publication-time proof. Original publication timestamps reuse G005's documented browser results. Current Help Center displayed dates do not prove historical unchanged content.

Earlier bounded web searches used full A/S1/S2 addresses, site:gamdom.com with their exact address prefixes, and exact addresses with Gamdom excluding explorer domains. They located explorer labels and third-party inventory, no direct official full-address attribution within that search coverage. Search results were not exported as a deterministic corpus, and this negative finding is not exhaustive. Only saved HTTP bodies are offline-reproducible acquisitions. Text scans exclude images, scripts, login-only pages and omitted search results. No absence-of-ownership claim is made.

Ethereum comparison: canonical USDT/USDC/DAI/USD1 source events, blocks 26177200–26184449 (Oct12 15:10:35–Oct13 15:24:35). Incident ledger selection follows G010's bounded E1 records. BNB B reconstruction is G011 blocks 127400000–127444806 (Oct13 12:07:45–17:43:53), zero measured opening; S1 comparison ends at 127429999 and partly overlaps reported incident window. A earlier BNB provenance and native baselines are not extended. Ethereum and BNB samples remain separate; no daily frequency anomaly or lifetime recipient activation conclusion is drawn.

No accounts, deposits, private customer records, outreach or new downstream/OMFT searches were used. Each assertion is limited to its original receipt/RPC/explorer/cryptographic/documentary evidence basis; current public labels remain third-party claims. Reproducibility relies on immutable parent inputs whose SHA-256 hashes are in source_register.json.
''')
md('blocker_report.md','''# Remaining blockers

The decisive blocker is evidentiary, not lack of additional downstream tracing: no independently authenticated full-address Gamdom custody attribution or transaction-specific unauthorized instruction was recovered for A/S1/S2. Public breach statements do not enumerate the audited wallets or source outflows. Selected key continuity resolves technical signing only. Baseline windows are short and incomplete for source permissions/native activity. No complete USD loss valuation or all-network source accounting is available.

HTTP and archive outcomes are preserved verbatim under evidence/. Failed or unusable results do not establish missing transactions or nonexistent ownership records. G014's OMFT boundary is retained and not searched again. The bounded accounting and maximum comparison add substantive analytical value, so this checkpoint may be published as a qualified evidence audit; Medium/X remain HOLD. Narrow further research to archival ownership/custody evidence rather than expanding financial associations.
''')
# preserve source map after all references
ref('','source_register.csv');dump('source_register.json',dict(new_acquisitions=sources,frozen_inputs=refs))
print('principal',len(rows),'transactions',len({(x['chain_id'],x['transaction_hash']) for x in rows}));print(json.dumps(summary,indent=2))
