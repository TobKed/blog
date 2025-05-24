# Agentic AI helper

## TODO

- [x] - handle duplicates
- [ ] - remove crewAI, use firecrawl for simplifcation
- [ ] - handle youtube videos with YT api?
- [ ] - make better prompts
- [ ] - use strategy pattern to handle links with different libraries like crewAI, firecrawl, BS4

## Helper snippets

```shell
python insert_links_tool.py content/posts/2025_05_test.md "https://www.doliver.org/articles/rss-as-a-skill" "https://alifeengineered.substack.com/p/visibility-without-bragging-a-practical" --verbose
python insert_links_tool.py content/posts/2025_05_test.md "https://csirmazbendeguz.github.io/2025/04/15/you-dont-need-composite-primary-keys.html" "https://djangochat.com/episodes/michael-kennedy" --verbose
python insert_links_tool.py content/posts/2025_05_test.md "https://www.youtube.com/watch?v=wz0GQbkrr1Q" "https://adamj.eu/tech/2025/04/07/django-whats-new-5.2/" --verbose
python insert_links_tool.py content/posts/2025_05_test.md "https://csirmazbendeguz.github.io/2025/04/15/you-dont-need-composite-primary-keys.html" "https://djangochat.com/episodes/michael-kennedy" --verbose

python insert_links_tool.py content/posts/2025_05_test.md "https://www.youtube.com/watch?v=wz0GQbkrr1Q" "https://adamj.eu/tech/2025/04/07/django-whats-new-5.2/"  "https://youtu.be/oP49EHjMTHc" "https://testdouble.com/insights/from-engineer-to-consultant-the-powerful-shift-from-inward-to-outward-focus?urm_source=test" "https://www.youtube.com/watch?v=xtmc-gTSPeA" --verbose

python insert_links_tool.py content/posts/2025_05_test.md "https://adamj.eu/tech/2025/04/07/django-whats-new-5.2/" --verbose

python insert_links_tool.py content/posts/2025_05_test.md "https://www.youtube.com/playlist?list=PL0MRiRrXAvRiSmPn_LDdhDbtZwu6g4xct/" "https://www.youtube.com/watch?v=-Zp5ffZDaRc" "https://m.youtube.com/watch?v=CIBmVXteOcI" "https://den.dev/blog/pihole/" --verbose
python insert_links_tool.py content/posts/2025_05_test.md "https://www.youtube.com/playlist?list=PL2Uw4_HvXqvb98mQjN0-rYQjdDxJ_hcrs" "https://www.youtube.com/watch?v=-Zp5ffZDaRc" "https://m.youtube.com/watch?v=CIBmVXteOcI" "https://den.dev/blog/pihole/" --verbose
```

```shell
python bulk_process_links.py batch_links.md
```
