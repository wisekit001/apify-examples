# Data: which brands AI assistants recommend (19 Nov 2026)

`ai-recommendations-2026-11-19.csv` has one row per AI answer. The run asked ChatGPT, Perplexity and Gemini (official APIs, web search on) 5 buying questions in 3 categories: project management tools, small-business CRMs and website builders. That's 45 answers.

| Column | Meaning |
|---|---|
| `category` | project-management, small-business-crm or website-builder |
| `engine` | chatgpt, perplexity or gemini |
| `question` | The question asked |
| `tracked_brands_named_in_order` | Which of the 9 tracked brands in that category the answer named, in order of first mention |
| `cited_domains` | Domains the answer cited as sources |

Write-up and limits: https://dev.to/wisekit. Collected with the [AI Visibility Tracker](https://apify.com/wisekit/ai-search-visibility-tracker) (disclosure: we built it). One run on one day; AI answers vary between runs. CC BY 4.0: reuse it freely with a link back.
