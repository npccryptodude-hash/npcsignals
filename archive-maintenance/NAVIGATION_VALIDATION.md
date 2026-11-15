# navigation validation / 15 november 2026

[quality report](REPORT.md)

## local completeness

all 16 registered subject entrances occur in the research index and resolve to existing documents. all new reader-page local targets resolve, including exact workbook filenames with spaces and parentheses. the 40 remaining missing targets are confined to the two preserved source copies documented in the source-link guide.

## actual github desktop rendering

the published review branch was opened in github without signing in, at a measured viewport of 1363 × 936 pixels. the research index rendered as readable lists with descriptive links and work-status labels. the index-to-gamdom and index-to-frogman paths were followed in the live interface; both six-part reader entrances rendered, and the return link to the index worked. the desktop index and gamdom page were inspected visually.

this is a sample of actual rendered navigation, not a claim that every historical dataset or every technical report was visually reviewed.

## mobile acceptance remains pending

the new index uses single-column lists rather than a wide table. that improves its structure for narrow screens, but is not a substitute for a mobile test.

a local chromium launch was blocked by the execution environment’s socket restriction. the available remote browser did not expose viewport resizing, and a device-mode keyboard attempt did not change its measured viewport. no real mobile-width result was obtained. **mobile rendering is not certified by this audit and remains an acceptance item.**

## external source availability

383 normalized unique markdown urls were checked with bounded unauthenticated get requests: 346 returned 200. the [full availability report](EXTERNAL_LINKS.md) separates access restrictions, rpc-method limitations, server errors and dated 404 responses. this does not validate a source’s content or authenticate an archived capture.
