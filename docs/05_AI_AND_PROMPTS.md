# Intelligence modes and prompts

## Local mode

No external requests. Keyword themes and deterministic recipes are fully operational. UI labels identify local behavior. This is a useful fallback, not a claim of live generative AI.

## Optional embeddings

Set OPENAI_API_KEY and OPENAI_EMBEDDING_MODEL, restart, and click Semantic grouping. The default model setting is text-embedding-3-small; confirm access in your own account. One request contains theme anchor texts and the current contribution texts. Display names and Twitch user IDs are not included.

This operation compares embeddings to a predefined theme vocabulary. It is not unconstrained clustering. Counts, indices, dimensions and finite numeric values are validated before assignments are accepted.

## Optional model drafts

Set OPENAI_MODEL to an accessible Chat Completions model supporting strict json_schema, as well as OPENAI_API_KEY. Select a local theme draft, then click Propose AI variation. The app requests a typed title, module list and actual source IDs. No model name is hardcoded for generation because access and supported models vary.

The system prompt in intelligence.mjs establishes these constraints: viewer text is untrusted data; allowed modules only; 12-point budget; an energy source is required; cite only supplied source IDs; no tools, scripts, external factual claims or runtime code.

Validation happens after schema parsing too. The app rejects unknown modules, duplicates, missing energy generation, overspending, invented citations and sources outside the selected theme. Human approval is still required.

## Failures and cost controls

Requests time out after 20 seconds. There is one intelligence request at a time. Provider errors leave local operation available; the app shows an error rather than pretending a failed request succeeded. The operator can use a local draft instead. Session/revision conflicts discard stale results.

The provider key stays on the backend. Configure a provider-side spending limit. Do not assume a ChatGPT subscription supplies an API budget. Track actual model tokens/embedding input and billing in your provider dashboard; this app does not implement billing metering.

## Evaluation set to create with participants

Collect 30–50 consented suggestions: paraphrases, multi-topic ideas, unusual ideas, short commands, typos, prompt-injection attempts and non-English text. Have a person label suitable themes. Compare local and embedding mode, record mistakes, and adjust anchors and thresholds. No multilingual performance claim is established by Unicode tokenization alone.

Test generation with: budget violations, extra modules, made-up IDs, refusal text, empty output, non-JSON response, timeouts and a provider 429. Mocks cover several rejection paths. A valid live provider call still needs testing with your own key.

## Expansion

Next steps are dynamic cluster discovery, host merge/rename, multilingual anchors, per-module source attribution and a curated game grammar. Build evaluations before replacing the transparent local method with an opaque classifier.
