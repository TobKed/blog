known_invalid_urls = {
    # known for sure to be good
    "mailto://tobiaszkedzierski@gmail.com",
    "https://www.snowflake.com/",
    # TODO
}

selenium_links_registry = {
    # DOIST
    "https://blog.doist.com/deep-work/": (
        "/html/body/div[3]/article/div[1]/header/h1",
        "The Complete Guide to Deep Work",
    ),
    "https://blog.doist.com/burnout-career-life-reset/": (
        "/html/body/div[3]/article/div[1]/header/h1",
        "Burned Out and Fantasizing About a Big Life Reset? Start Here",
    ),
    "https://blog.doist.com/how-to-plan-your-day/": (
        "/html/body/div[3]/article/div[1]/header/h1",
        "The Complete Guide to Planning Your Day",
    ),
    "https://blog.doist.com/productivity-shame/": (
        "/html/body/div[3]/article/div[1]/header/h1",
        "How To Stop Feeling Productivity Shame",
    ),
    "https://blog.doist.com/organize-your-life/": (
        "/html/body/div[4]/article/div[1]/header/h1",
        "How to Organize Your Life",
    ),
    "https://blog.doist.com/how-to-prioritize/": (
        "/html/body/div[3]/article/div[1]/header/h1",
        "How to Prioritize When There’s Always More To Do",
    ),
    "https://blog.doist.com/unconventional-goal-setting/": (
        "/html/body/div[3]/article/div[1]/header/h1",
        "Forget About SMART Goals: 5 Unconventional Goal Setting Methods to Try Instead",
    ),
    "https://blog.doist.com/business-writing/": (
        "/html/body/div[3]/article/div[1]/header/h1",
        "How to Write For the Way Your Coworkers Actually Read",
    ),
    "https://blog.doist.com/cognitive-biases-time-management/": (
        "/html/body/div[3]/article/div[1]/header/h1",
        "7 Cognitive Biases That Make Us Suck at Time Management",
    ),
    "https://blog.doist.com/replace-meetings-twist/": (
        "/html/body/div[3]/article/div[1]/header/h1",
        "When to Take Real-time Meetings Async",
    ),
    # OTHER
    "https://blog.cloudflare.com/october-2021-facebook-outage/": (
        "/html/body/div[1]/main/article/h1",
        "Understanding How Facebook Disappeared from the Internet",
    ),
    "https://arc.dev/blog/remote-work-productivity-tips-ad27ns7c15": (
        "/html/body/div/div[2]/div[1]/div[2]/article/h1",
        "Remote Work Productivity Hacks: 33 Best Tips From Experts",
    ),
    "https://a16z.com/2021/05/27/cost-of-cloud-paradox-market-cap-cloud-lifecycle-scale-growth-repatriation-optimization/": (
        "/html/body/div[1]/div[2]/main/div/div/article/main/div/header/h1",
        "The Cost of Cloud, a Trillion Dollar Paradox",
    ),
    "https://www.baeldung.com/ops/docker-memory-limit": (
        "/html/body/div[1]/div[2]/div/div/div[1]/article/header/div/h1",
        "Setting Memory And CPU Limits In Docker",
    ),
    "https://labs.ebury.rocks/2020/07/07/dynamic-variant-analysis-python/": (
        "/html/body/div/div[1]/div/div[3]/div/div[2]/article/div[2]/div[2]/p",
        "Dynamic Variant Analysis with Python",
    ),
    "https://flyonthecloud.com/pl/flytalks/talk-to-my-backend-milosz-kusiciel/": (
        "/html/body/div[1]/div[1]/div[1]/div[1]/h1",
        "Talk to my backend, czyli Miłosz Kusiciel o platformie chmurowej GCP",
    ),
    "https://www.theregister.com/2020/12/10/google_cloud_over_run/": (
        "/html/body/div[2]/div[4]/h1",
        "Google Cloud (over)Run: How a free trial experiment ended with a $72,000 bill overnight",
    ),
    "https://www.behance.net/gallery/94053021/Her-Impact-self-development-app-for-women": (
        "/html/body/div[1]/div[1]/div/div[2]/div[1]/div/div[1]/div/div[2]/div[1]/figcaption/span",
        "Her Impact | self-development app for women",
    ),
    "https://www.lifehack.org/articles/productivity/10-tips-help-you-more-efficient-working-from-home.html": (
        "/html/body/main/div[2]/div/div[1]/article/h1",
        "How to Work From Home: 10 Tips to Stay Productive",
    ),
    "https://supermemo.guru/wiki/Genius_checklist": (
        '//*[@id="firstHeading"]',
        "Genius checklist",
    ),
    "https://www.lifehack.org/articles/productivity/16-everyday-habits-highly-productive-people.html": (
        "/html/body/main/div[2]/div/div[1]/article/h1",
        "16 Everyday Habits of Highly Productive People",
    ),
    "https://suade.org/dev/12-requests-per-second-with-python/": (
        "/html/body/main/div/article/h1",
        "12 requests per second",
    ),
    "https://www.jhanley.com/google-cloud-understanding-gcloud-configurations/": (
        "/html/body/div[4]/div/div[1]/div/div[1]/h1/a",
        "Google Cloud – Understanding Gcloud Configurations",
    ),
    "https://blog.detectify.com/2020/11/10/common-nginx-misconfigurations/": (
        "/html/body/div[5]/div[1]/div/h1",
        "Common Nginx misconfigurations that leave your web server open to attack",
    ),
    "https://cacm.acm.org/opinion/articles/252174-the-10-best-practices-for-remote-software-engineering/fulltext": (
        "/html/body/div[3]/div/section/div[2]/h1",
        "The 10 Best Practices for Remote Software Engineering",
    ),
    "https://www.economicsdiscussion.net/management/productivity-meaning-concept-formulas/32324": (
        "/html/body/div[2]/div/div/div/section/article/header/h1",
        "Productivity: Meaning, Concept, Formulas, Techniques, Measurement and Advantages",
    ),
    "https://emshea.com/post/writing-python-unit-tests-lambda-functions": (
        "/html/body/section/div/div/div[2]/div/div[1]/div[1]/h1",
        "Writing unit tests for Lambda functions in Python",
    ),
    "https://www.lastweekinaws.com/blog/the-17-ways-to-run-containers-on-aws/": (
        "/html/body/div[1]/div[1]/div[1]/div[1]",
        "The 17 Ways to Run Containers on AWS ",
    ),
    "https://labs.ebury.rocks/2020/10/09/sql-spotlight-on-django-problems/": (
        "/html/body/div/div[1]/div/div[3]/div/div[2]/article/div[2]/div[2]/p",
        "SQL, spotlight on Django problems",
    ),
    "https://pybit.es/articles/ast-intro/": (
        "/html/body/div[1]/div/div/main/article/header/h1",
        "Abstract Syntax Trees in Python",
    ),
    "https://arnon.dk/5-things-i-learned-developing-billing-system/": (
        "/html/body/main/article/header/div/h1",
        "5 things I learned while developing a billing system",
    ),
    "https://www.singlestoneconsulting.com/blog/infrastructure-as-code-at-enterprise-scale/": (
        "/html/body/div[1]/main/div/div/div/h1",
        "Infrastructure as Code at Enterprise Scale: Identify the Right Approach for Your Organization",
    ),
}
