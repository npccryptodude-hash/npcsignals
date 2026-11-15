# mobile and reader acceptance / 15 november 2026

[quality report](REPORT.md) · [final acceptance review](ACCEPTANCE_REVIEW.md) · [measurements](MOBILE_MEASUREMENTS.json)

## actual responsive-width test

the earlier inability to obtain a narrow viewport is superseded by this review. chromium’s ordinary browser zoom produced **454 × 312** and **340 × 234 css-pixel viewports**, measured from the live page. github’s actual responsive layout was exercised; no custom html approximation or style override was used. browser zoom was restored to 100% afterwards.

this is a narrow-width reflow and navigation test. it does not emulate an iphone user agent, safari, touch targets, screen-reader behavior or a physical phone. desktop viewport checks from the earlier pass remain separately applicable.

| page or subject | widths tested | result |
| --- | --- | --- |
| repository homepage and rendered project identity | 340 and 454 | text wraps; archive entrance works |
| research index | 340 and 454 | single-column links; all 16 subjects remain listed |
| frogman | 340 and 454 | six-part entrance readable; evidence links available |
| gamdom | 340 and 454 | six-part entrance readable; direct loss/ownership links retested |
| zyrox | 340 and 454 | summary and evidence routes readable |
| glitch | 340 and 454 | original receipt and explanation links retested |
| gen z movements | 340 and 454 | comparative-research entrance readable |
| norway welfare | 340 and 454 | english/norwegian reports and sources reachable |
| presidential claims | 340 and 454 | workbook choices and limits readable |
| ai performance narratives | 340 and 454 | archived-audit entrance readable |

25 observations include initial measurements and retests. at 340 css pixels, article client/scroll widths were both 271; at 454, both were 383. no sampled entrance or homepage/index article overflowed horizontally. all sampled entrance articles contained **zero tables**. narrow-screen text wrapping was also inspected visually.

technical ledgers and original receipts remain technical source documents. the preserved original glitch response is a minified json line in github’s read-only source textbox; horizontal navigation there is a source-format limitation, not a wide table forced onto the reader entrance. the companion explanation and consolidation audit are linked separately.

## practical reader walkthroughs

these were **agent-performed task walkthroughs using three reader perspectives**, not tests with three recruited human participants. counts refer to successful content-link activations from the rendered repository homepage. scrolling, page resets between tasks and browser-automation setup are excluded; back actions and external cookie choices are stated separately. keyboard activation of a link counts as the same navigation choice as one click.

| perspective and task | observed route | count and outcome |
| --- | --- | --- |
| no technical background: find what gamdom documents and what remains unknown | homepage → research index → gamdom entrance | 2 link activations; purpose, documented movements and unresolved ownership visible |
| no technical background: read the accounting boundary | same route → loss-accounting explanation | 3 link activations after the navigation fix; no checkpoint-code interpretation required |
| school pupil: find documented norway findings | homepage → index → norway entrance → english report | 3 link activations; scope, findings and limitations reachable |
| school pupil: inspect the original budget document in the same session | report → browser back → source list → ministry document landing → read document | cumulative 6 content-link activations, plus 1 back action and 1 necessary-cookie choice; original ministry chapter opened |
| journalist: inspect the preserved primary glitch transaction response | homepage → index → glitch entrance → original transaction response | 3 link activations after the fix; saved response accessible with result, slot and signatures in github’s read-only source view |

on the school route, the official ministry document was reached at `https://www.regjeringen.no/en/documents/meld.-st.-1-2025-2026/id3126584/?ch=1`. this verifies the route to the source, not every archive claim derived from it.

## obstacles and fixes

1. the old gamdom G015 readme names analytical files as plain text. direct loss-accounting and wallet-ownership links were added to the existing case entrance; the frozen readme was not edited.
2. the older glitch technical overview links its visual story but names technical source files as text. the existing case entrance now links the visual explanation, original receipt and consolidation audit directly. the journalist route was repeated successfully.
3. github’s long branch/file headers and vertical scrolling remain part of its interface. the case entrances do not require opening the file tree, understanding git or selecting a raw checkpoint code.
4. large source tables, workbooks and the minified original response can require horizontal reading or a download once the reader deliberately enters the technical layer. original formats were preserved.
5. external source sites may add a cookie choice, access restriction or later change. the observed ministry route succeeded; earlier external-availability exceptions remain dated observations.

## acceptance

**passed:** sampled narrow-width reflow, case navigation, direct original-source route and the three practical walkthroughs, with the stated scope. **accepted test limits:** no physical-device, safari or recruited-human usability certification. these limits no longer leave a generic “mobile not tested” blocker; they define the actual test performed.
