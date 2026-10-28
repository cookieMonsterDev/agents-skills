# Document review checklist

Use this checklist for technical documentation, instructions for use, model cards, risk management files, quality management systems, FRIAs, post-market monitoring plans, AI use policies and contracts with model suppliers.

Check two things for each document: that it contains what the AI Act requires, and that it matches what the system actually does. Documentation that describes oversight, logging or accuracy the code does not deliver is a finding. When both a document and code are in scope, cross-check them against the step 2 inventory.

## Technical documentation (Art. 11, Annex IV)

- [ ] General description: intended purpose, provider, version, hardware and software it runs on, how it interacts with other systems
- [ ] Development process: design choices, architecture, pre-trained components and their provenance, training methods
- [ ] Data: datasheets for training, validation and test data, with provenance, labelling, cleaning and bias examination
- [ ] Human oversight measures (Art. 14) and the technical means that help deployers interpret outputs
- [ ] Accuracy, robustness and cybersecurity metrics, with test logs and reports signed and dated
- [ ] Risk management system (Art. 9) and changes made over the lifecycle
- [ ] Harmonised standards or other specifications applied
- [ ] EU declaration of conformity and the post-market monitoring plan

## Instructions for use (Art. 13)

- [ ] Provider identity and contact
- [ ] Intended purpose, and the circumstances of foreseeable misuse that may cause risk
- [ ] Declared accuracy levels and metrics, robustness and cybersecurity, and what can affect them
- [ ] Performance on the specific persons or groups the system is meant for
- [ ] Input data specifications
- [ ] Human oversight measures, including how to interpret outputs
- [ ] Expected lifetime, maintenance and updates
- [ ] How deployers collect, store and interpret the logs (Art. 12)

## Risk management (Art. 9)

- [ ] Known and foreseeable risks to health, safety and fundamental rights, under intended use and foreseeable misuse
- [ ] Risks found through post-market monitoring fed back in
- [ ] Measures for each risk, residual risk judged acceptable, and the reasoning
- [ ] Testing against predefined metrics, including real-world testing where used (Art. 60)
- [ ] Impact on people under 18 and other vulnerable groups considered

## Quality management system (Art. 17)

- [ ] Regulatory compliance strategy, including conformity assessment and handling of modifications
- [ ] Design, development, quality control and testing procedures
- [ ] Data management procedures
- [ ] Post-market monitoring, incident reporting and communication with authorities
- [ ] Record-keeping, resource management and an accountability framework
- [ ] Proportionate to the organization's size; simplified for SMEs and small mid-caps

## Art. 6(3) assessment

- [ ] Names the Annex III point concerned and the Art. 6(3) condition relied on
- [ ] Shows the system does not profile natural persons
- [ ] Dated before placing on the market, and registered under Art. 49(2)

## Fundamental rights impact assessment (Art. 27)

- [ ] Deployer processes in which the system is used, and the period and frequency of use
- [ ] Categories of persons and groups likely affected
- [ ] Specific risks of harm to those groups, taking the provider's instructions into account
- [ ] Human oversight measures per the instructions for use
- [ ] Measures if risks materialise, including governance and complaint mechanisms
- [ ] Results notified to the market surveillance authority; an existing DPIA reused where it covers the same ground

## Post-market monitoring plan and incident procedure (Art. 72, 73)

- [ ] Data collected on performance throughout the lifetime, including from deployers
- [ ] Interaction with other AI systems analysed where relevant
- [ ] Serious-incident definition, clock from awareness, and the 2, 10 and 15 day deadlines
- [ ] Investigation, corrective action and cooperation with authorities

## GPAI model documentation (Art. 53, Annex XI, XII)

- [ ] Annex XI: model description, architecture, parameters, training process, data sources, compute and energy, evaluation results
- [ ] Annex XII for downstream providers: capabilities, limitations, acceptable use, integration requirements
- [ ] Copyright policy, including how text-and-data-mining opt-outs are identified and honoured
- [ ] Public training-content summary on the Commission template
- [ ] Code of Practice signature or an alternative demonstration of compliance

## Transparency notices and labels (Art. 50)

- [ ] User-facing AI-interaction notice, and its placement at first interaction
- [ ] Deepfake and AI-generated text labels: wording, placement, and how editorial review exemptions are documented
- [ ] Notice to people exposed to emotion recognition or biometric categorisation

## AI policies and contracts (Art. 4, 25, 26)

- [ ] AI literacy measures: who is trained on what, matched to role and the systems used
- [ ] Contracts with upstream model or component suppliers give the information, capabilities and access needed to meet the AI Act (Art. 25(4))
- [ ] Deployer policies assign oversight to competent people with authority and support (Art. 26(2))
- [ ] Workers and their representatives informed before a high-risk system is used at work (Art. 26(7))
