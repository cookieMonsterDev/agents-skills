# Code review checklist

Use this checklist for repositories, diffs, model training and inference pipelines, API specs, infrastructure code and user interfaces. Code shows what the system does; it rarely shows the intended purpose, the deployment context or the conformity records. Pair each technical finding with the organizational question it raises.

For a diff or pull request, review the changed AI behaviour and its direct interactions: a new model call, prompt, decision path, output channel or dataset. Note pre-existing issues you pass by, but keep them separate from the change's findings.

## 1. Discover AI systems and models

Search before reading. Adapt the patterns to the codebase's language and naming, and read every hit in context, since names alone produce false positives.

```bash
# Model APIs, SDKs and inference runtimes
rg -n -i '(openai|anthropic|bedrock|vertexai|generativeai|mistral|cohere|huggingface|transformers|langchain|llama_?index|ollama|vllm|onnxruntime|tensorflow|torch|sklearn|xgboost|lightgbm|coreml|tflite)'

# Model artifacts, registries and training code
rg -n -i '(model_?card|\.safetensors|\.onnx|\.pt\b|\.pkl|mlflow|wandb|sagemaker|fine_?tun|train_test_split|\.fit\(|trainer\.train|dataset)'

# Decisions about people (Annex III signals)
rg -n -i '(score|rank|eligib|approv|reject|credit|loan|insur|hire|candidate|resume|cv_|applicant|exam|grade|proctor|fraud|risk_?level|benefit|asylum|visa)'

# Biometrics and emotion (Art. 5, Annex III point 1, Art. 50(3))
rg -n -i '(face_?(rec|detect|match|embed)|facial|biometric|voiceprint|emotion|sentiment|affect|liveness|gait)'

# Generated content and conversational interfaces (Art. 50)
rg -n -i '(chat(bot)?|assistant|completion|generate_?(image|audio|video|text)|text_?to_?(image|speech|video)|tts|diffusion|synthes|deepfake|voice_?clon)'
```

Also inspect: feature stores, prompt templates and system prompts, evaluation suites, data loaders and dataset manifests, labelling tools, decision thresholds and rule overrides, admin and review consoles, and vendor contracts or SDK configuration for third-party models.

Done when the inventory in SKILL.md step 2 lists each system and model, its purpose signals, where it runs and who receives its output.

## 2. Checks

Each check names its main articles. Severity guidance is in [report-template.md](report-template.md#severity).

### Prohibited practices (Art. 5)

- No emotion inference on employees or students, except for medical or safety reasons.
- No biometric categorisation inferring race, political opinions, trade-union membership, religion, sex life or orientation.
- No scraping of facial images from the internet or CCTV to build recognition databases.
- No scoring of people on social behaviour that leads to unrelated or disproportionate detrimental treatment.
- No dark patterns or subliminal techniques that materially distort decisions, and no targeting of age, disability or socio-economic vulnerability to cause harm.
- Generative systems carry safeguards against producing non-consensual intimate imagery and CSAM.

### Classification and intended purpose (Art. 6, Annex III)

- The use the code implements matches the documented intended purpose; a system deployed for an Annex III use the provider did not intend is a role-change finding (Art. 25(1)(c)).
- Where an Art. 6(3) derogation is claimed, the code confirms the narrow role: no profiling, a human makes the decision, the output is preparatory.

### Record-keeping and logging (Art. 12, 19, 26(6))

- Each use logs a timestamp, the input or a reference to it, the output, the model and version, and the person or process that acted on the output.
- For remote biometric identification, logs hold the period of use, reference database, matched input and the identity of the people who verified the result (Art. 12(3)).
- Logs are tamper-evident, retained at least six months, and themselves minimise personal data (cross-check with `gdpr-compliance`).

### Human oversight (Art. 14, 26(2))

- A reviewer can see the output with enough context to interpret it: confidence, contributing factors, known limitations.
- A reviewer can override or reverse an output, and the override is recorded.
- A stop control halts the system safely, and a fallback path exists when it is stopped.
- Interfaces counter automation bias: no pre-selected "approve" default, no hidden confidence, no forced throughput that rules out real review.

### Data governance (Art. 10, 4a)

- Datasets have provenance records: source, licence or legal basis, collection date, and processing steps (cleaning, labelling, enrichment).
- Bias examination runs on relevant groups, with results stored; special-category data used for it is segregated, access-controlled and deleted after correction (Art. 4a).
- Training, validation and test splits are separated and versioned so results are reproducible.

### Accuracy, robustness and cybersecurity (Art. 15)

- Evaluation measures the declared accuracy metrics, and a release gate blocks regressions.
- Inputs are validated; prompt injection, data poisoning, adversarial examples and model extraction are addressed in the threat model.
- Online-learning systems guard against feedback loops from their own biased outputs.
- Model artifacts and weights are access-controlled and integrity-checked.

### Transparency to people (Art. 50, 26(11), 86)

- Chatbots and voice agents tell users they are talking to an AI, at the latest at first interaction, unless obvious from context.
- Generated audio, image, video and text carry machine-readable marking: C2PA content credentials, watermarks or metadata, robust where technically feasible.
- Deepfakes and AI-generated text published on matters of public interest carry a visible disclosure.
- People subject to emotion recognition or biometric categorisation are informed.
- Decisions about people from Annex III systems inform the affected person, and an explanation path exists (Art. 86).

### GPAI model providers (Art. 53, 55)

- Training-data pipelines honour machine-readable rights reservations (robots.txt and similar opt-outs) and record sources for the training-content summary.
- Model documentation and the downstream-provider information pack (Annex XI, XII) are generated from the training and evaluation records.
- For systemic-risk models: adversarial testing, incident tracking and weight security controls exist.

### Post-market monitoring and incidents (Art. 72, 73)

- Production telemetry captures performance drift, error rates and complaints per group.
- A path routes suspected serious incidents to the provider within the Art. 73 deadlines.

## 3. Map findings to fixes

Give fixes in the codebase's own idiom: the existing audit logger, the review queue, the evaluation harness, the existing content-credential or watermarking library. Note when a fix needs an organizational decision first (intended purpose, the Art. 6(3) assessment, choice of conformity route).
