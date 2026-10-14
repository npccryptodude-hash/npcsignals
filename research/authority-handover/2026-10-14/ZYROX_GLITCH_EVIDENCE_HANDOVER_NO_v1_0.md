# NPCsignals | Teknisk overleveringsrapport

**ZYROX og GLITCH: offentlige transaksjonsspor, kontrollsignaler og spørsmål for videre etterforskning**  
**Dokument-ID:** NPCS-HO-2026-10-14-v1.0  
**Forskningsstopp:** 14. oktober 2026 UTC  
**Status:** Saksorientering og teknisk henvisningspakke. Ikke anmeldelse, bedragerikonklusjon eller identifisering av person.

> **Mandat:** NPCsignals følger offentlige blokkjedeoverføringer og dokumenterer hvor det offentlige transaksjonssporet slutter, slik at autoriserte myndigheter eventuelt kan be børser om intern bokføring og lovlig tilgjengelige kundeopplysninger. Walletforbindelser er ikke personidentiteter.

## 1. Sammendrag for saksbehandler

**GLITCH — CONFIRMED.** 12. oktober 2026 kl. **17:51:18 UTC**, slot **456135125**, ble **116 513 762,335674 GLITCH** overført fra **seks kildetokenkontoer** til **én mottakende tokenkonto i samme Solana-transaksjon**, med **syv signaturer**: seks kildeautoriteter og mottakerens eier/gebyrbetaler. Fem tilleggskilder bidro med **46 513 762,335674 GLITCH**, ved siden av en tidligere dokumentert overføring på 70 millioner GLITCH. Alle seks kildesaldoer gikk til null. En felles transaksjon dokumenterer koordinert gjennomføring, ikke nødvendigvis felles menneskelig kontroll. [G1]

**ZYROX × GLITCH — CONFIRMED adresseoverlapp.** Den eksakte Solana-nøkkelen `6hR7GwHpdHbJgNJAagm64KMsMYu8mR6ExzmbE5N8wv1N` inngår i ZYROX-forskningen og mottok **435,460959353 SOL** fra en GLITCH-relatert motpart 12. oktober kl. **17:52:55 UTC**. Avsenders midler var blandet; hele beløpet kan ikke betegnes som identifiserte GLITCH-salgsinntekter. Felles operatør og endelig mottaker er **UNRESOLVED**. [G2]

**Binance-merket infrastruktur — CONFIRMED overføringer, SUPPORTED børsattribusjon.** Fire SOL-overføringer fra U300, totalt **472,929423997 SOL**, samt én USDT-overføring autorisert av 56HEQ på **995,831502 USDT**, nådde samme offentlige nøkkel eller historiske tokenkontoeier: `5tzFkiKscXHK5ZXCGbXZxdw7gTjjD1mBwuoFbhUvuAi9`. Bitquery og Solscan merker den som Binance-infrastruktur, men Binance har ikke bekreftet historisk kontroll eller intern kundekreditering. September-overføringene fant sted **før lanseringene**; oktober-overføringen er ikke tilskrevet utelukkende GLITCH-proveny. [B1]

**Bruksverdi:** Et etterprøvbart, avgrenset utgangspunkt for autorisert forespørsel om historisk kontroll, intern avstemming, transaksjons-ID-er og eventuelle kundeopplysninger. Ikke dokumentasjon på at en navngitt promotør har begått lovbrudd.

## 2. Bevisstandard

| Nivå | Betydning |
|---|---|
| **CONFIRMED** | Direkte reproduserbar observasjon fra bevart primærmateriale innen angitt testomfang |
| **SUPPORTED** | Underbygget av kilder, men avgjørende primærbekreftelse mangler |
| **CLAIMED** | Påstand eller markedsføring med begrenset kildebekreftelse |
| **UNRESOLVED** | Ikke tilstrekkelig bevis for konklusjon |
| **NOT ASSESSED** | Ikke undersøkt |

En signatur dokumenterer kontroll over kryptografisk nøkkel ved signering, ikke personidentitet. Overføring til børsmerket adresse er ikke automatisk et kundenummer eller et kundedepositum. Gebyrsponsing, delt infrastruktur eller overføringer mellom kontoer identifiserer ikke nødvendigvis eieren.

## 3. GLITCH: dokumentert hendelsesforløp

| UTC 12.10.2026 | Hendelse |
|---|---|
| 16:22–16:23 | Dokumenterte SOL-finansieringstransaksjoner til fem nye kildeautoriteter; eldre rapporter beskriver bredere strukturert finansiering |
| 16:32:33 | Skaperassosiert konto `Ft2XtprBymZsGwYUMjsLN6z8WZzguTVa5rFYSuN41S8i` ervervet 70 millioner GLITCH |
| 17:51:18 | Seks kilder sender samlet 116 513 762,335674 GLITCH i én signert transaksjon |
| 17:51:19 | Stor selger selger 594 968 303,379290 GLITCH for brutto 132,890991957 WSOL; eksakt proveniens til tokenene i salget ikke fullt bevist |
| 17:52:55 | GLITCH-relatert B-wallet overfører 435,460959353 SOL til den i ZYROX registrerte 6hR7-nøkkelen |

**Konsolideringssignatur:**  
`3ttmcRNck85nUEcnaTZ3nmMWpq9sAdCwjq8EF56Zz4wzsi3dz2AB1G18FibKKmqNzShVexFVanogoAUSJeJXojy1`

**Slot** 456135125; **outer instructions** 2–7; **gebyrbetaler/mottakereier:** `8hiMXA1UHYUAeW6gd6q1XQLWzZkQL48znqgdgY1388B7`; **gebyr** 35 700 lamports. Mottakerens tokenbeholdning endret seg fra **2 936 950,790841** til **119 450 713,126515 GLITCH**. [G1]

Et arkivert Telegram-skjermbilde viser GLITCH-kontraktadressen publisert/redigert hos «Kytro Insider Calls». Bildet viser redigeringstid, ikke sikkert første publiseringstidspunkt og tidssone. Materialet brukes derfor **ikke** som bevis for at transaksjoner fant sted før første offentlige CA-deling.

## 4. Eksakt sammenfall mellom sakene

**Felles wallet:** `6hR7GwHpdHbJgNJAagm64KMsMYu8mR6ExzmbE5N8wv1N`.

I ZYROX-dokumentasjonen har adressen blant annet mottatt **468,432649156 SOL** fra 6cn og **175,588375882 SOL** fra F1dC. I GLITCH-saken mottok den **435,460959353 SOL** fra `F2khA1QZooUzidyycMzpJ6x38eQBxuDq4UrvdUUiSwuo` (B).

**GLITCH-til-6hR7-signatur:**  
`61v1KxQkjSpMTenBBKE3nCSyh4EBZFV8gffPdaNojEjXvvzavdCqEbHqWQ8ewf3eWPTiqrsLbUErdpbPzDFGp13B`

B signerte og betalte gebyret. 6hR7 var **mottaker, ikke signer**. B hadde øvrige innbetalinger, slik at det innsendte beløpet ikke automatisk kan beskrives som 100 % GLITCH-proveny. En avgrenset ny test av syv GLITCH-signere og fem finansieringskilder ga **ingen eksakte adresse-treff** i to tidligere ZYROX-forskningstrær. Dette er ikke et bevis på uavhengige personer. [G1][G2]

## 5. Fem historiske overføringer til Binance-merket infrastruktur

**Mottakernøkkel:** `5tzFkiKscXHK5ZXCGbXZxdw7gTjjD1mBwuoFbhUvuAi9`  
**U300 avsender:** `8zHcWujHhyJri3CRTcWUGmT5WSRdwW7xrns3WTTkPGvS`  
**56HEQ USDT-autorisator:** `56HEQykziUkwvpK5uPzFrRbGD4Ek8HdWgjgeDvNmDoEJ`.

| ID | UTC | Beløp | Slot | Full transaksjonssignatur |
|---|---|---|---|---|
| BE001 | 2026-09-30 17:03:07 | 52,383204688 SOL | 452026176 | `3tPBHCeM4Y86RETWoAhmFKD1JjVs4GWduMxzsYwSstKktAKg3jovJbr54dUhaHfh1L8vxQJiGJ3BVgYhRs92vgWY` |
| BE002 | 2026-09-30 17:06:00 | 292,066250817 SOL | 452026821 | `4SxWP8XZRb3z1zg5dcTCsvGvMNtBm92zfibZ2KHySAVCZ34nTN9st6MrcaY7NnDfC8dsRsCMyiX6wMf4KoB9YsNm` |
| BE003 | 2026-09-30 17:12:00 | 105,583014451 SOL | 452028164 | `4xyFCL3f67ejRXTf3NZHgXScUVfXdCiWPsx9NNM1UWeNnmvMWcAFzGzYzGYapWFgHyFBD1aNmM9WDte7DbkpYnGe` |
| BE004 | 2026-10-14 06:00:01 | 22,896954041 SOL | 456730989 | `4m6gaPuwQnwN7KFSeCi3SzaqJzyj6JPzL5sMjq2c3gYuniYAqg3kZMPsseDdomzVJaVjZF3LPXYyHXAqeKKfSuYb` |
| BE005 | 2026-09-24 12:03:01 | 995,831502 USDT | 450023141 | `3QrJH49NS39jAtvEPn8BxCNGqkiwMZk1kSDJ2GU8f8jVU5GxVzxzd9bKSLx2KYkm7G6mPLP8Vsk3S94TuZMiayz2` |

**Rute A:** U300 autoriserte de fire SOL-overføringene til nøyaktig 5tz. September-summen **450,032469956 SOL** predaterer begge casenes rapporterte tokenlanseringer. Oktoberoverføringen **22,896954041 SOL** hadde blandet finansieringshistorikk.

**Rute B:** Den felles case-walleten 6hR7 sendte **4,028124 + 991,803278 = 995,831402 USDT** til en konto historisk eid av 56HEQ 24. september. Et separat **0,000100 USDT** påslag fra en **annen** konto forklarer beløpsforskjellen før 56HEQs utgående **995,831502 USDT** til tokenkontoen historisk eid av 5tz. Adresse med liknende 6hR7-prefix er **ikke** den samme casenøkkelen. Disse betalingene fant sted før tokenlanseringene. [B1]

**Attribusjonsgrense:** Bitquery har merket 5tz Binance hot wallet, og Solscan viser «Binance 2». Dette støtter en børs-infrastrukturhypotese, men er **ikke** en Binance-autorisert historisk custodian- eller kundekontobekreftelse. Interne kontoregnskap og eventuell kontoidentitet krever lovlig ekstern avklaring.

## 6. Målrettede spørsmål til Binance via autorisert prosess

1. Kontroller om Binance historisk disponerte mottakernøkkelen og relevant USDT-tokenkonto på hvert av tidspunktene BE001–BE005.
2. Avstem hver signatur til eventuelle interne transaksjons- og bokføringsreferanser: kundeinnbetaling, intern overføring, treasury, ukreditert innbetaling eller annet.
3. Hvis en kundekonto ble kreditert: dokumenter etter gjeldende lovhjemmel relevant kundekonto, instruksjonsgiver, historisk disponering og lovlig tilgjengelige KYC-opplysninger.
4. Undersøk om avsender U300, 56HEQ eller særskilt gebyrbetaler var børsinfrastruktur, før noen person- eller kundeslutning trekkes.
5. Be om bevaring av berørte logger og interne poster etter korrekte juridiske formaliteter. NPCsignals har ikke kontaktet børsen og krever ikke privat informasjon.

**Separat MEXC-spor:** MEXCs offisielle adresseoversikt oppgir `ASTyfSima4LLAdDgoFGkgqoKowG1LZFDr9fAQrg7iaJZ`. Tidligere forskning omtaler åtte utgående USDT-betalinger på samlet 477,442575 USDT, men fullstendige åtte signaturer og råkvitteringer er ikke samlet i den aktuelle rapportrevisjonen. Disse skal ikke brukes som ferdig verifisert depositumskjede eller bevis for kunden bak utbetalingen. [M1]

## 7. Informasjon fra eventuell anmelder / fornærmet

En person som mener seg villedet, bør levere sin **egen** separate dokumentasjon til relevant myndighet:
- Token, eksakt kjøpssignatur, eventuelt salg, dato/tid, beløp, betalt valuta og egen wallet.
- Den konkrete påstanden som ble lagt til grunn; original innlegg-URL, meldings-ID og skjermbilder med kildeproveniens.
- En kort redegjørelse for hvordan påstanden påvirket kjøpsbeslutningen.
- Kvitteringer/utskrifter for egne inn- og utbetalinger, og eventuelt faktisk tap.
- Kontaktopplysninger **kun via godkjent, privat myndighetskanal**.

ZYROX-arkivet har skjermbilder av konkrete salgsfremmende utsagn; disse må leses med dokumentert kildekvalitet og uten forhåndskonklusjon om lovbrudd. For GLITCH er eksakt originalpost som lover «fair launch» eller «no insiders» ikke fullt kildebekreftet. Ikke oppgrader den til dokumentert premiss uten original. [M1]

**Personvern:** Ikke publiser personers navn, KYC, tap, private wallettilknytninger eller anmeldelsesinnhold på åpent GitHub. Disse håndteres gjennom autoriserte kanaler.

## 8. Bevisarkiv, integritet og kildeindeks

Binance v2.0-arkivet har **384 offentlige bevisfiler**, individuelt gjenhentet og verifisert mot Git-objekter og SHA-256. **383 manifestposter passerte**; den siste (384.) filen er manifestet selv. Den opprinnelige verifieren ga **fem PASS** i en uavhengig Linux-kjøring. Windows-portabilitetsfeil i en sti-sammenligning er særskilt dokumentert, mens native Windows-verifikasjon av rettingsforslaget ikke er vurdert. Kontrollen beviser integritet av arkivert data etter innhenting, ikke børsens kundebokføring. [B2]

Kildene er låst til offentlige Git-commiter:

- **[G1]** [Kontroll- og signaturundersøkelse 14.10.2026](https://github.com/npccryptodude-hash/npcsignals/tree/5259354b80c5c8f37cba4fb2b179bf44e6141a2e/research/zyrox-investigation-post-freeze/control-attribution-2026-10-14/) — seks kilder, syv signaturer, fem finansieringskvitteringer og avgrenset negativ test.
- **[G2]** [GLITCH v0.11: eksakt wallet-overlapp](https://github.com/npccryptodude-hash/npcsignals/blob/5259354b80c5c8f37cba4fb2b179bf44e6141a2e/research/glitch-investigation/GLITCH_v0.11_confirmed_ZYROX_overlap.md) — ZYROX/GLITCH-koblingen ved 6hR7.
- **[G3]** [Tidlig GLITCH-finansiering](https://github.com/npccryptodude-hash/npcsignals/blob/5259354b80c5c8f37cba4fb2b179bf44e6141a2e/research/glitch-investigation/GLITCH_early_launch_coordination_pre_audit_v0.1.md).
- **[B1]** [Binance Evidence Package v2.0](https://github.com/npccryptodude-hash/npcsignals/tree/46f5f3df4e4e20de712c48105533cd99e7f3fc28/research/evidence/binance-v2.0-2026-10-14/) — femoverføringsledger, arkiver, JSON-kvitteringer og verifikator.
- **[B2]** [Uavhengig verifikasjonsrapport](https://github.com/npccryptodude-hash/npcsignals/blob/b21e5ec2467ff35cb06369d05f5170f5913a697e/research/audits/binance-v2.0-2026-10-14/VERIFICATION_REPORT.md).
- **[M1]** [Påstands- og kilderevisjon v0.2](https://github.com/npccryptodude-hash/npcsignals/blob/5259354b80c5c8f37cba4fb2b179bf44e6141a2e/research/glitch-investigation/GLITCH_ZYROX_claim_vs_chain_audit_v0.2.md).

**Ved overlevering:** Oppgi full signatur, tokenmint, beløp, tidssone (UTC), slot, eksakt Git-commit og filbane. Bevar nye kvitteringer separat og uendret med dato og SHA-256. Myndigheter bør gjennomføre egne primærkontroller ved beslutninger med rettslige følger.

## 9. Konklusjon

NPCsignals har dokumentert en koordinert GLITCH-overføring, en eksakt adresse som går igjen i begge tokenundersøkelsene, og historiske transaksjoner til børsmerket infrastruktur. Dette gir et **etterprøvbart teknisk startgrunnlag** for mulig videre etterforskning og oppslag i interne børsregistre.

Det er ikke fastslått at en bestemt promotør eller operatør står bak begge tokenene, at de historiske børsbetalingene er proveny fra tokenlanseringene, eller at det foreligger straffbart bedrageri.

**PUBLIC TRACE DOCUMENTED / AUTHORIZED RECORDS REQUIRED**

*NPCsignals · https://npcsignals.com · Connections are not identities. Visibility is not verification.*
