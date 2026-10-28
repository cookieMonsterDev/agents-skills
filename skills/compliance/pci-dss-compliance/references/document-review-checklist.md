# Document review checklist

Use this checklist for security policies and procedures, scoping records, network and data-flow diagrams, SAQs and AOCs, service-provider records, targeted risk analyses, incident response plans and other documents that describe a payment environment.

Check two things for each document: that it contains what PCI DSS requires, and that it matches what the system actually does. A diagram that omits a flow the code performs, or an SAQ type the integration does not fit, is a finding. When both a document and code are in scope, cross-check them against the step 2 inventory.

## Scope and diagrams (1.2.3, 1.2.4, 12.5.1, 12.5.2)

- [ ] Network diagram shows every connection between the CDE and other networks, including wireless
- [ ] Data-flow diagram shows every account-data flow across systems and networks
- [ ] Inventory of in-scope system components is current
- [ ] Scope is confirmed at least every 12 months and after significant change (every six months for service providers, 12.5.2.1), with data locations and segmentation controls recorded
- [ ] Out-of-scope claims name the segmentation control and its latest test (11.4.5)

## SAQ and AOC

- [ ] The SAQ type matches every payment channel and its integration; each eligibility criterion is true for the system as built
- [ ] SAQ A merchants with an embedded payment iframe show how the script-attack criterion is met (FAQ 1588)
- [ ] Every "In Place with CCW", "Not Applicable" and "Not Tested" response is explained, with a compensating controls worksheet where used
- [ ] AOC is signed, dated within the last 12 months and names the PCI DSS version

## Service providers (12.8, 12.9)

- [ ] List of every TPSP that handles account data or could affect its security, with the services provided
- [ ] Written agreements in which each TPSP acknowledges its responsibility for the account data it handles (12.8.2)
- [ ] Due diligence before engagement and annual monitoring of each TPSP's compliance status, such as a current AOC (12.8.3, 12.8.4)
- [ ] Responsibility matrix showing which requirements the TPSP, the entity, or both manage (12.8.5)
- [ ] Service providers give customers that acknowledgement and responsibility information (12.9)

## Policies and procedures (x.1.1, x.1.2, 12.1)

- [ ] Each of requirements 1-12 has documented, current policies and procedures, known to the people who apply them
- [ ] Roles and responsibilities for each requirement are assigned
- [ ] Information security policy reviewed at least every 12 months
- [ ] Data retention and disposal policy covers every store of account data and SAD, with a purge at least quarterly for data past retention (3.2.1)
- [ ] Key-management procedures cover generation, distribution, storage, cryptoperiods, retirement and split knowledge (3.6.1, 3.7)
- [ ] Payment-page script inventory with written justifications (6.4.3)

## Risk analyses and customized approach (12.3)

- [ ] A targeted risk analysis exists for each requirement where the entity sets the frequency, reviewed at least every 12 months (12.3.1)
- [ ] Each customized-approach control has its own targeted risk analysis and controls matrix (12.3.2, Appendices D and E), and the entity is validating by ROC
- [ ] Cipher suites and protocols in use, and hardware and software technologies, are reviewed at least every 12 months (12.3.3, 12.3.4)

## Incident response (12.10)

- [ ] Plan covers roles, communication including card-brand and acquirer notification, containment, recovery and data backup
- [ ] Plan is tested at least every 12 months and personnel are trained
- [ ] Procedures cover finding stored PAN where it is not expected (12.10.7)
- [ ] Alerts from security monitoring, including 11.6.1 tamper detection, feed the plan

## Security awareness (12.6)

- [ ] Program on hire and at least every 12 months, covering phishing and social engineering

## Other documents

For architecture proposals, vendor assessments and design specifications: build the flow inventory from the text, then check the integration and candidate SAQ, SAD handling, storage and protection of the PAN, service providers and their AOCs, segmentation, MFA and logging. Record each silence in the document as an evidence gap.
