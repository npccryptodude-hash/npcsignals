# Protocol Analysis

**Freeze:** 2026-10-01  
**Status:** DRAFT

## 1. Primary procedure

Tennessee's published lethal-injection protocol uses pentobarbital as the execution drug.

The protocol describes a **Primary Set A** containing saline, two pentobarbital syringes and a final saline flush. The two pentobarbital syringes together contain approximately **5 grams**.

## 2. Contingency

The protocol provides a backup pathway if the prisoner remains alive after the primary administration and the required waiting period and examination.

Operationally:

**Primary Set A → waiting period / examination → if still alive → Backup Set B**

The backup set is therefore an explicit contingency for failure of the primary set.

## 3. The edge case

Before Pike's execution, her legal team served a Request for Admission asking the state to admit that:

- the protocol did not provide medical care, resuscitation, or emergency medical intervention in the event of a failed or botched execution; and
- the protocol's only contingency if the prisoner was not deceased after Primary Set A and the five-minute waiting period was preparation and administration of Backup Set B.

This is significant as evidence that the endpoint scenario was explicitly raised before the execution. The request itself is documented. This file does **not** characterize the request as a state admission unless a corresponding response is independently verified.

## 4. Post-attempt state statement

On 2026-09-30, TDOC stated that:

- every step of the state's lawful, established execution protocol had been followed;
- the protocol did not allow additional procedures beyond what had been carried out that evening; and
- Pike had been transported to an off-site medical facility.

This establishes a protocol endpoint independent of any speculation about the medical cause of failure.

## 5. System representation

**PRIMARY PROCEDURE**  
Set A

↓  

**CHECK**  
Waiting period and examination

↓  

**CONTINGENCY**  
Set B if prisoner remains alive

↓  

**SECOND FAILURE**  
Prisoner remains alive

↓  

**PROTOCOL ENDPOINT**  
No additional execution procedure authorized under the published protocol

↓  

**OUTSIDE MEDICAL CARE**

## 6. What this analysis does not establish

This analysis does not establish:

- that the intended systemic dose was actually delivered;
- that IV infiltration occurred;
- that the drug was improperly prepared;
- that pentobarbital itself failed pharmacologically;
- that any one physiological factor caused the outcome.

Those questions remain unresolved pending further evidence and the ordered review.

## Sources

See [sources.md](sources.md).
