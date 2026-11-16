YEARS = "10+"

SUMMARY = [
    "Senior fullstack engineer with 10+ years designing, leading and building JavaScript-heavy products - from single-page e-commerce platforms to AI-assisted tools",
    "Works across the whole stack: React and Vue interfaces, Node.js services and REST APIs, serverless backends on Cloudflare Workers, and the databases behind them",
    "Solid experience in designing, leading and implementing technology projects",
    "Expert in JavaScript frameworks and libraries such as React, Angular, Node.js and Knockout",
    "Backend development with Node.js, Express.js and Nest.js, REST API design, and serverless edge APIs on Cloudflare Workers",
    "Advanced knowledge in OOP concept, design patterns",
    "Experience in working with Kanban boards and Scrum environment, in individual or team development processes",
    "Strong debugging, analytical, and problem-solving abilities",
    "Ability to learn new frameworks and technologies quickly and independently",
]

CORE = ("JavaScript/HTML5/CSS3, TypeScript, React, Vue, Node.js, Nest.js, Next.js, Cloudflare Workers, "
        "REST API, PostgreSQL, Knockout, Angular, OCC, OSF, flexible team player")

SKILLS = [
    ("Programming languages:", "JavaScript, TypeScript, PHP (basic)"),
    ("Backend &amp; Cloud:", "Node.js, Express.js, Nest.js, REST/RESTful API, Cloudflare Workers, Workers KV, Cron Triggers, OAuth 2.0, Telegram Bot API, Webhooks, Passport.js"),
    ("Web technologies and Frameworks:",
     "React, Angular, KnockoutJS, React-Native, Reactstrap, Bootstrap, jQuery, HTML5, CSS3, SASS/LESS, SCSS, "
     "Material-UI, React Material UI, Redux, Redux-Thunk, Redux-Saga, Redux Toolkit, Redux-Form, Oracle OSF, "
     "Oracle Commerce Cloud, Chart.js, Postman, BEM Methodology, REST, Webpack, Figma, Adobe XD, Next.js"),
    ("Databases:", "MySQL, MongoDB, PostgreSQL, Oracle"),
    ("Project / Task Management Tools:", "Atlassian, JIRA, Trello, Asana"),
    ("Other frameworks and Tools:", "Docker, Kubernetes"),
    ("Version control systems:", "GIT, GitHub, GitLab, Bitbucket"),
]

SOFT = [
    "Strong analytical skills to understand complex business processes and develop optimal solutions",
    "Attention to detail, ensuring high-quality code and system reliability",
    "Effective communication and collaboration with teams, clients, and technical specialists to align on solutions",
    "Quick adaptability to new technologies and evolving project requirements",
    "Problem-solving mindset with the ability to research, analyze documentation, and work independently",
]

CERTS = [
    ("Claude Code in Action", "Anthropic · Certificate of Completion · No: fqtagrttnnpe", "https://verify.skilljar.com/c/fqtagrttnnpe"),
    ("Introduction to Agent Skills", "Anthropic · Certificate of Completion · No: fqei3pomez7u", "https://verify.skilljar.com/c/fqei3pomez7u"),
    ("Introduction to Model Context Protocol", "Anthropic · Certificate of Completion · No: vn2ssbar447h", "https://verify.skilljar.com/c/vn2ssbar447h"),
    ("Mentoring", "iTechArt · Training course · February 2022 - for engineers who lead and grow junior developers", "https://github.com/sergevei/sergevei.github.io/blob/master/certificates/itechart-mentoring.pdf"),
]

GTM = "Participated in daily meetings, analyzed user stories, identified and resolved gaps in user business requirements"
REFAC = "Redesigned and refactored the source code to provide better scalability, maintainability, and code readability"
DEPLOY = "Worked with project deployment and publishing"

EXPERIENCE = [
    dict(name="Salesmsg", period="09/2023 – present", role="Senior Software Developer", team="Team of 50+",
         stack="JavaScript (ES6), TypeScript, Vue, React, Node.js, Express.js, PostgreSQL, Redis, REST API, Docker, Kubernetes, HTML5, SASS/SCSS, MobX, MUI, Web Services, Google Tag Manager, GitHub, Figma, Webflow, Webflow CMS, Webflow API, Claude Code (plugins, skills, agents), MCP",
         desc="Two-way SMS marketing software for sending, receiving, and managing business texts and calls. On the backend - Node.js microservices with REST APIs over PostgreSQL that power messaging, contacts and campaigns.",
         bullets=[
             "Developing Node.js / TypeScript microservices and REST API endpoints for messages, contacts and campaigns",
             "Designing PostgreSQL schemas, writing migrations and optimizing queries and indexes",
             "Processing background jobs and webhooks through Redis queues",
             "Implementing Google Tag Manager",
             "Working with project deployment and publishing",
             "Building reusable code for future use",
             "Redesigning and refactoring the source code to provide better scalability, maintainability, and code readability",
             "Participating in daily meetings, analyzing user stories, identifying and resolving gaps in user business requirements",
         ],
         extra=dict(label="Parallel project:",
                    desc='salesmessage.com website (12/2023 – present, Webflow). Three months into the product work also took over the company\'s marketing website <a href="https://www.salesmessage.com/" color="#0F766E">salesmessage.com</a> - from development and integrations to AI tooling for the marketing and design teams.',
                    bullets=[
                        "Developing and maintaining Webflow components, pages and CMS collections",
                        "Integrating the site with third-party services and the product: analytics, tag management, forms and custom code",
                        "Optimizing performance, Core Web Vitals and SEO",
                        "Building Claude plugins, skills and AI agents that let the marketing and design teams create pages, components and blog posts on their own",
                        "Writing project documentation: component library, page-building guides and workflows",
                        "Full Webflow deployment and publishing support",
                    ])),
    dict(name="BSoft", period="05/2022 – 09/2023", role="Senior Software Developer", team="Team of 10+",
         stack="JavaScript (ES6), React, Node.js, Express.js, PostgreSQL, Sequelize, JWT, REST API, Docker, HTML5, SASS/SCSS, MobX, Reactstrap, Web Services, Google Tag Manager, GitHub, Figma, AI system, MUI",
         desc="A web application for managing facade projects - recording building data, calculating wind loads, and giving sales teams self-serve tools so they don't have to loop in engineers for routine tasks. The backend is a Node.js REST API over PostgreSQL that stores projects and building data and runs the wind-load calculations.",
         bullets=[
             "Built a Node.js / Express.js REST API for projects, buildings and calculation results",
             "Designed the PostgreSQL data model and migrations with an ORM (Sequelize)",
             "Moved the wind-load calculations to the server and validated input data",
             "Implemented JWT authentication and role-based access for sales and engineering teams",
             "Integrated AI system",
             DEPLOY, "Built reusable code for future use", REFAC, GTM,
         ]),
    dict(name="Oracle OSF Platform", period="01/2022 – 05/2022", role="Senior Software Developer", team="Team of 10+",
         stack="JavaScript, React, Node.js, Express.js, REST API, SSR, Postman, Bootstrap, SCSS, HTML5, Agile, Endeca, Bitbucket, Jira, Oracle Commerce Cloud, Oracle Commerce Cloud API",
         desc="A server-rendered storefront built on Oracle's Open Storefront Framework, designed to render pages quickly with SEO-friendly, single-page delivery. A Node.js layer renders the pages on the server and talks to the Oracle Commerce Cloud APIs.",
         bullets=[
             "Developed Node.js server-side rendering and middleware on top of the Oracle Commerce Cloud REST APIs",
             "Built server-side endpoints for catalog, cart and checkout data with response caching",
             DEPLOY, "Ensured the technical feasibility of UI/UX designs", "Updated OCF configuration", REFAC,
             "Pixel-perfect development", GTM,
         ]),
    dict(name="AI Legal Assistant", period="05/2021 – 01/2022", role="Senior Software Developer", team="Team of 5+",
         stack="JavaScript (ES6), React, Node.js, Express.js, PostgreSQL, JWT, REST API, HTML5, SASS/SCSS, MobX, Reactstrap, Web Services, Google Tag Manager, GitHub, Figma, AI system",
         desc="An AI legal assistant that understands and simplifies complex legal documents - contracts, rental agreements, mortgage papers - by removing legal jargon and summarizing lengthy text. The goal was to scale the client's existing Chrome extension into a full web platform with its own backend: a Node.js API that processes uploaded documents and stores them with their summaries in PostgreSQL.",
         bullets=[
             "Built a Node.js / Express.js REST API for document upload, text extraction and AI summarization",
             "Designed the PostgreSQL schema for users, documents and summaries",
             "Implemented authentication with JWT and secure file storage",
             "Integrated AI system", "Implemented Google Tag Manager", DEPLOY, REFAC, GTM,
         ]),
    dict(name="Ponnrest", period="01/2021 – 05/2021", role="Senior Software Developer", team="Team of 15+",
         stack="JavaScript (ES6), React, Node.js + Express.js, PostgreSQL, Sequelize, JWT, REST API, HTML5, SASS/SCSS, Redux-Thunk, Redux Toolkit, Reactstrap, Web Services, Google Tag Manager, GitHub, Figma",
         desc="A restaurant table-reservation platform with distinct roles - client, administrator, manager, super-administrator - each with different functionality and permissions for viewing, approving, modifying, and canceling orders. The backend is a Node.js REST API over PostgreSQL with role-based access control.",
         bullets=[
             "Developed a Node.js / Express.js REST API for restaurants, tables and reservations",
             "Designed the PostgreSQL schema and queries that prevent double-booking of tables",
             "Implemented JWT authentication and role-based permissions for clients, managers and administrators",
             "Mobile-first development", "Implemented Google Tag Manager", DEPLOY, REFAC, GTM,
         ]),
    dict(name="Gratis", period="05/2019 – 01/2021", role="Senior Software Developer", team="Team of 20+",
         stack="JavaScript, KnockoutJS, jQuery, Postman, AJAX, Bootstrap, SCSS, HTML5, Agile, Endeca, Bitbucket, Jira, Oracle Commerce Cloud, Oracle Commerce Cloud API",
         desc="An e-commerce SPA for Turkey's biggest cosmetics retailer, with flexible faceted product search, online purchases, a loyalty program, a store locator, and account management.",
         bullets=[
             "Implemented live GTM (Google Tag Manager)", "Developed sales cards", DEPLOY,
             "Ensured the technical feasibility of UI/UX designs", "Updated OCC configuration", REFAC,
             "Pixel-perfect development", GTM,
         ]),
    dict(name="Westland", period="03/2018 – 05/2019", role="Middle Frontend Developer", team="Team of 7+",
         stack="JavaScript, KnockoutJS, jQuery, AJAX, Bootstrap, SCSS, HTML5, Endeca, Bitbucket, Jira, Oracle Commerce Cloud, Oracle Commerce Cloud API, Postman",
         desc="A retail platform for gardening, bird, and pet-care products, supporting multiple payment methods (PayPal, Barclays, Visa, Mastercard, and more).",
         bullets=[
             DEPLOY, "Ensured the technical feasibility of UI/UX designs", "Updated OCC configuration",
             "Discussed new features and ways of improving existing functionality", "Pixel-perfect development", GTM,
         ]),
    dict(name="Interactive Maps", period="11/2017 – 03/2018", role="Middle Frontend Developer", team="Team of 10+",
         stack="Vue, JavaScript, HTML5, SCSS, Material-UI, GitHub, Jira, Bootstrap, Figma",
         desc="A Bing Maps app with custom HD layers (BlueSky, GraySky, high-res birdsEye), a drawing tool, and split-screen comparison between two different map layers.",
         bullets=[
             "Developed and designed map tools", "Designed split-screen functionality", "Designed the 3D/2D maps model",
             "Analyzed and recommended changes to existing code, frameworks, and applications",
             "Applied the most recent and useful Vue approaches and tools for the best application performance and security",
             GTM,
         ]),
    dict(name="PocPortal", period="06/2017 – 11/2017", role="Middle Frontend Developer", team="Team of 5+",
         stack="React, JavaScript (ES6), HTML5/CSS3, Sass, Node.js + Express.js, Bootstrap, Material UI, Redux-Thunk, Redux Toolkit, Chart.js, Web Services, GitHub, Twilio",
         desc="A news platform for searching and posting news across categories, with comments, ratings, a built-in messenger, and a weather widget that displays local weather by IP.",
         bullets=[
             "Developed a well-structured, maintainable, and easy-to-understand application backend while adhering to defined coding standards",
             "Designed built-in live chat", "Developed responsive graph widgets",
             "Ensured the technical feasibility of UI/UX designs", GTM,
         ]),
    dict(name="GlHealthCare", period="10/2016 – 06/2017", role="Junior Frontend Developer", team="Team of 5+",
         stack="Vue, HTML5/CSS3, Node.js, SCSS, Material UI, Twilio, Web Services, Payment APIs (PayPal, credit card, American Express, Citibank)",
         desc="A platform letting medical providers sell increased patient access - calls or texts directly to the provider, expedited appointments - plus membership creation and payment management.",
         bullets=[
             "Mobile-first development", "Ensured the technical feasibility of UI/UX designs",
             "Integrated services (Twilio, Payment APIs)",
             "Developed a well-structured, maintainable, and easy-to-understand application frontend and backend", GTM,
         ]),
    dict(name="TCourses", period="01/2016 – 09/2016", role="Junior Frontend Developer", team="Team of 10+",
         stack="React, JavaScript/TypeScript, Node.js, Express.js, Redux-Saga, Redux Toolkit, Reactstrap, Web Services, Webpack, MongoDB, Bitbucket, Jira, Adobe XD, Next.js",
         desc="A platform for organizing courses and training, with candidate selection, lectures, tests, homework, and mentor chat - students receive a certificate after completing the course.",
         bullets=[
             "Developed a well-structured, maintainable, and easy-to-understand application backend while adhering to defined coding standards",
             "Discussed new features and ways of improving existing functionality",
             "Designed and implemented highly scalable microservice-based services",
             "Mobile-first development", "Designed the PDF certificate generator",
         ]),
]

OBYN_INTRO = ("OBYN - a family of free web apps designed and built fullstack, end to end: offline-first React PWAs on the "
              "frontend and a serverless backend on Cloudflare Workers. User data stays in the user's own Google Drive: "
              "no sign-up and no ads.")
OBYN_BACKEND = ("Edge API on Cloudflare Workers - OAuth 2.0 code exchange and token refresh with the client secret kept on "
                "the server (long-lived Google Drive sign-in), plus a Telegram reminder bot for OBYN. Endpoints check the origin "
                "and validate input; the server keeps no user records except the opt-in data the reminder bot needs.")

PROJECTS = [
    dict(name="OBYN", tag="Expense tracker in BYN", url="https://obyn.by/",
         desc="Personal finance tracker: expenses by period with charts, budgets and automatic conversion to USD and EUR at the official National Bank of Belarus rate. Runs entirely in the browser.",
         bullets=["Spending charts by category and period, budget tracking and period comparison",
                  "Currency conversion synced with the National Bank exchange-rate API",
                  "Cross-device sync through the user's own Google Drive, backups to JSON and CSV; installable PWA with full offline mode",
                  "Telegram reminder bot @OBYNBot: a daily digest about upcoming and overdue bills and days without receipts at the hour the user picks, and a “Nearest bills” button with the three closest payments"],
         sections=[("Telegram bot:", [
             "Bot backend on Cloudflare Workers: a Telegram webhook verified with a secret-token header, an hourly Cron Trigger and storage in Workers KV",
             "Reminders at each user's local hour: the app sends the device time zone, the worker computes the local time and date with Intl, daylight saving included; at most one digest a day",
             "Privacy by design: one-tap linking through a t.me deep link with a random 256-bit key that the server keeps only as a SHA-256 hash; bill names and amounts are left out when the user's data is encrypted; /stop or “Turn off” in the app deletes everything",
             "KV metadata holds the hour and time zone, so the cron reads only the records that are due; users who blocked the bot are removed automatically",
             "Covered by Vitest tests against a mocked Telegram API and Workers KV",
         ])],
         stack="React 18, TypeScript, Vite, Redux Toolkit, React Router, PWA (Workbox), IndexedDB / localStorage, Google Drive API (OAuth 2.0), Chart.js, NBRB Exchange Rates API, Cloudflare Workers, Telegram Bot API (webhooks), Cron Triggers, Workers KV, Wrangler"),
    dict(name="OBYNTasker", tag="Task planner by periods", url="https://tasker.obyn.by/",
         desc="Task planner for people who plan work and life in weeks and sprints: a Kanban board, a filtered list, a \"Focus for today\" view and an archive with period results.",
         bullets=["Kanban board with drag-and-drop and mobile swipe; \"Focus for today\" with the most urgent and overdue tasks first",
                  "Period archive with completion rate, carried-over and finished tasks",
                  "Google Drive sync between devices, Excel export, offline-first PWA"],
         stack="React 18, TypeScript, Vite, Redux Toolkit, React Router, PWA (Workbox), IndexedDB / localStorage, Google Drive API (OAuth 2.0), dnd-kit, SheetJS, Cloudflare Workers, Wrangler"),
    dict(name="OBYNAuto", tag="Car maintenance by mileage", url="https://obyn.online/",
         desc="Car maintenance log: oil, filters and other services by mileage and dates. Enter the odometer reading and the app predicts what to replace and when. Russian and English UI, freemium model.",
         bullets=["Recurring services with km and/or month intervals, ready-made presets, next-service date forecast based on average mileage",
                  "Subscription API: verifies the user's Google token, reads the paid plan from Workers KV and starts a 30-day trial",
                  "Server-side localization at the edge: renders the localized head (title, Open Graph, JSON-LD) by country for SEO"],
         stack="React 18, TypeScript, Vite, Redux Toolkit, React Router, PWA (Workbox), IndexedDB / localStorage, Google Drive API (OAuth 2.0), i18next, SheetJS, Cloudflare Workers, Workers KV, Wrangler"),
    dict(name="OBYNHabits", tag="Habit tracker", url="https://habits.obyn.by/",
         desc="Habit tracker with daily check-ins, streaks and monthly results - including non-daily schedules like Mon/Wed/Fri or \"3 times a week\".",
         bullets=["\"Today\" ring with one-tap check-in; current and best streaks that respect custom schedules",
                  "Monthly summaries and history; Google Drive sync, backups, installable offline PWA"],
         stack="React 18, TypeScript, Vite, Redux Toolkit, React Router, PWA (Workbox), IndexedDB / localStorage, Google Drive API (OAuth 2.0), Recharts, date-fns, Cloudflare Workers, Wrangler"),
    dict(name="OBYNSplit", tag="Debts &amp; shared expenses", url="https://split.obyn.by/",
         desc="Splits shared expenses and tracks debts between friends in BYN, USD and EUR with conversion at the National Bank rate - trips, flatmates, group gifts.",
         bullets=["Debts and shared bills split equally or by exact amounts; groups with automatic \"who owes whom\" settlement",
                  "Multi-currency balances synced with the National Bank exchange-rate API; Google Drive sync, offline mode, no sign-up"],
         stack="React 18, TypeScript, Vite, Redux Toolkit, React Router, PWA (Workbox), IndexedDB / localStorage, Google Drive API (OAuth 2.0), NBRB Exchange Rates API, Cloudflare Workers, Wrangler"),
    dict(name="OBYNWatch", tag="What to watch", url="https://watch.obyn.by/",
         desc="A watchlist for films, series and cartoons with ratings from 1 to 10 and advice on what to watch next, built from the user's own ratings and favourite genres. Russian and English UI, free.",
         bullets=["Search in the TMDB catalogue with posters and genres; recommendations from titles rated 7+ with the reason under each one",
                  "TMDB proxy on Cloudflare Workers: the API key stays on the server, allow-list of paths, edge caching with the Cache API; poster proxy for regions where the image CDN is blocked",
                  "Server-side localization at the edge with HTMLRewriter; Google Drive sync, offline mode, install as an app"],
         stack="JavaScript (ES2022), PWA (Service Worker), localStorage, Google Drive API (OAuth 2.0), TMDB API, Cloudflare Workers (edge API, Cache API, HTMLRewriter), Wrangler"),
]

CONTACTS = [("GitHub:", "github.com/sergevei", "https://github.com/sergevei"),
            ("LinkedIn:", "linkedin.com/in/siarhei-vei", "https://www.linkedin.com/in/siarhei-vei-310b24229"),
            ("Telegram:", "t.me/vsergeserge", "https://t.me/vsergeserge"),
            ("Portfolio:", "sergevei.github.io", "https://sergevei.github.io/")]
HOBBIES = "Playing volleyball, Cycling, Swimming"
