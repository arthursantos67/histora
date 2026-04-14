# Software Requirements Document (DRS) - Histora

**Project:** Histora - Academic Social Network for Historians of Education

---

## 1. Introduction

### 1.1 Purpose of the Document
The purpose of this Software Requirements Document (DRS) is to specify, in an exhaustive, rigorous, and unambiguous way, all functional and non-functional requirements, business rules, and architectural constraints for the development of the Histora platform. This document serves as the definitive technical contract that will guide the development team throughout the implementation cycle, ensuring that the final product meets academic needs with scalability, security, and robustness.

### 1.2 Problem the System Aims to Solve
The community of historians of education lacks a unified digital space that combines the rigor of an institutional repository with the dynamism of a social network. Currently, researchers are split between generic platforms (which dilute scientific focus) and static repositories (which do not foster debate and connection). Histora addresses the fragmentation of academic production and the difficulty of specialized networking by offering an environment where publication, versioning, and discussion occur in an integrated and moderated way.

### 1.3 Academic Context and Motivation
The system arises from the need to preserve humanity's memory through scientific rigor. The central motivation is to create a digital ecosystem that respects the traditions of historical research - such as peer review, rigorous citation, and evidence-based debate - transposing these practices into a modern interface. The platform must reflect seriousness, reliability, and specialization, distancing itself from superficial dynamics common in commercial social networks.

### 1.4 Macro Scope
Histora is a web platform that encompasses the creation of detailed academic profiles, a social feed focused on publications and debates, a robust system for submission and versioning of papers (with PDF support), connection mechanisms among researchers, and advanced moderation tools to ensure community integrity.

### 1.5 System and Strategic Objectives
The system's primary objective is to facilitate the circulation of academic production in the History of Education and promote qualified interaction among its authors. Strategically, Histora aims to become the main digital hub for this discipline, establishing an online academic governance standard that can, in the future, be expanded or replicated to other areas of the humanities.

### 1.6 Target Audience of the Document
This document is intended primarily for the technical team (full-stack developers, software architects, database engineers, and DevOps/Security specialists) responsible for implementation. Secondarily, it serves project stakeholders (initiators, academic coordinators) for scope validation and expectation alignment regarding what will be delivered in the Minimum Viable Product (MVP) and subsequent phases.

### 1.7 Initial Glossary of Terms
* **Endorsement:** Action equivalent to a qualified "like," indicating recognition of the academic value of a publication or comment.
* **Versioning:** The ability of an author to update the file (PDF) of an existing publication while keeping the history of previous versions accessible for traceability purposes.
* **Connection:** Bidirectional link between two researchers, established through invitation and acceptance, allowing a higher level of interaction and visibility.
* **Follow:** Unidirectional link in which a user chooses to receive updates from another researcher in their feed, with no approval required.
* **Academic Moderation:** Process of evaluating reports and content to ensure adherence to the platform's scientific code of conduct.
* **Co-authorship:** Association of multiple researchers to the same publication, requiring acceptance from all involved.

---

## 2. Product Vision

### 2.1 What the Platform Is
Histora is an academic social network and dynamic repository, designed exclusively for historians of education. The platform acts as a digital ecosystem where scientific rigor meets real-time collaboration, allowing researchers to publish papers, debate discoveries, and build professional networks in a safe and specialized environment.

### 2.2 Who It Exists For
The platform was conceived to serve the entire academic hierarchy of the History of Education: from senior researchers and university faculty seeking to disseminate their research and guide debates, to graduate students (master's and doctoral) and undergraduate students who need validated references and networking. Research institutions and historical archives are also part of the ecosystem as affiliation entities.

### 2.3 Value Proposition and Differentiators
Histora's value proposition lies at the intersection of academic formality and social fluidity. The platform is not just a repository because it does not merely store PDFs statically; it encourages continuous discussion around each publication through structured comments and transparent versioning. At the same time, it is not just a social network because it rejects vanity metrics and shallow engagement algorithms, prioritizing academic governance, rigorous moderation, and knowledge traceability.

The core academic differentiator is the publication versioning system, which recognizes that historical research is an iterative process. By allowing authors to update their work while preserving version history and prior debates, Histora reflects the true nature of scientific production.

### 2.4 Pains Solved and Opportunities Created
The system solves the pain of invisibility of ongoing research or research published in proceedings with restricted circulation, as well as the difficulty of finding peers researching highly specific topics. It creates opportunities for the establishment of organic research groups, interinstitutional collaborations, and democratization of access to validated historical knowledge, all under a code of conduct that prevents harassment and misinformation.

---

## 3. User Profiles / Personas / System Actors
The platform operates with a permissions model based on roles (Role-Based Access Control - RBAC), clearly defining the scope of action of each actor.

### 3.1 Visitor (Unauthenticated)
* **Objectives:** Explore the platform, discover relevant content, and assess whether registering is worthwhile.
* **Needs:** Fast access to publication abstracts and public profiles without login barriers.
* **Permissions:** View the landing page, search researchers and public publications, read abstracts and metadata.
* **Limitations:** Cannot download PDFs, cannot view comments, cannot interact (endorse, comment), has no personalized feed.
* **Usage Risks:** Automated extraction of public information (scraping).

### 3.2 Member (Authenticated Researcher)
* **Objectives:** Publish papers, build academic reputation, debate with peers, and stay up to date.
* **Needs:** Intuitive interface for PDF upload, detailed profile management, and relevant feed.
* **Permissions:** Create and edit full profile, submit publications, manage versions of their papers, endorse, comment, follow researchers, send connection invitations, report content.
* **Limitations:** Actions restricted to their own content and allowed interactions; no access to administrative dashboards.
* **Usage Risks:** Uploading third-party copyrighted content, inappropriate behavior in debates.

### 3.3 Moderator
* **Objectives:** Ensure the academic integrity of the platform and compliance with the code of conduct.
* **Needs:** Efficient tools for report analysis, context visualization, and sanction enforcement.
* **Permissions:** All Member permissions, plus: approve/reject new registrations, access report queue, hide/remove inappropriate publications or comments, issue warnings, temporarily suspend accounts.
* **Limitations:** Cannot change global system settings or permanently delete accounts without administrative review.
* **Usage Risks:** Moderation bias, arbitrary actions without documented justification.

### 3.4 Administrator
* **Objectives:** Manage the platform at a strategic and technical level, ensuring operation and evolution.
* **Needs:** Global metrics dashboards, full control over users and system settings.
* **Permissions:** Unrestricted access. Can manage roles (promote Member to Moderator), configure system parameters, access audit logs, make the final decision on moderation appeals, and permanently delete accounts.
* **Limitations:** Subject to privacy policies and LGPD regarding access to sensitive data (e.g., passwords, which must be hashed).
* **Usage Risks:** Improper access to private data, accidental changes to critical settings.

---

## 4. System Scope
Scope must be rigorously controlled to ensure delivery of a functional, scalable, high-quality product.

### 4.1 Included Scope (MVP and Phase 1)
* Complete authentication and authorization system (registration with approval, login, password recovery).
* Management of detailed academic profiles (personal information, affiliation, research areas).
* Submission of publications in PDF format with metadata extraction/insertion.
* Publication versioning system (revision history of the same paper).
* Chronological social feed based on connections and followed researchers.
* Academic interactions: endorsements (likes) and comments on publications.
* Connection (bidirectional) and follow (unidirectional) system among researchers.
* Global search for researchers, publications, and research areas.
* Moderation panel for registration approval and report management.
* Basic publication privacy and visibility settings.
* In-app notifications system for relevant events.

### 4.2 Excluded Scope (Will not be done in the initial version)
* Native mobile apps (iOS/Android). The platform will be exclusively responsive web.
* Integration with university legacy systems (institutional SSO, LTI).
* Direct messages (real-time private chat). *Justification: The initial focus should be public debate on publications.*
* Creation and management of complex Groups/Communities.
* Events module (calendar, registrations).
* Complex recommendation algorithms based on AI or Machine Learning.

### 4.3 Assumptions and Dependencies
* **Assumptions:** Users have basic digital literacy and access to stable internet connections for PDF upload/download. The academic community values rigorous moderation.
* **Dependencies:** Cloud storage service (e.g., AWS S3) for secure PDF hosting. Transactional email delivery service (e.g., SendGrid, AWS SES) for notifications and password recovery.

### 4.4 Constraints
* Maximum PDF upload size will be limited to 50MB to optimize storage costs and performance.
* The system must be developed using open-source technologies and established frameworks to accelerate development and facilitate maintenance.

---

## 5. Architectural Decisions (ADRs)
To ensure system scalability, security, and maintainability, the following architectural decisions (Architecture Decision Records - ADRs) have been established:

### 5.1 Backend: Python with Django and Django REST Framework (DRF)
* **Decision:** The backend will be developed using Python with the Django framework and Django REST Framework (DRF).
* **Reason:** Django provides native robustness against common vulnerabilities (SQL Injection, XSS, CSRF) and has a mature ORM that guarantees relational data integrity. DRF facilitates the creation of standardized and secure RESTful APIs.
* **Benefit:** High security by default, accelerated development due to Django's included batteries (admin panel, ORM, base authentication), and ease of maintenance.

### 5.2 Frontend: Next.js (React) with Server-Side Rendering (SSR)
* **Decision:** The frontend will be built with Next.js, a React framework, using Server-Side Rendering (SSR).
* **Reason:** SSR is vital to ensure indexing (SEO) of academic publications by search engines (Google Scholar, Google, etc.), which is a critical requirement for researcher visibility.
* **Benefit:** Better initial load performance, optimized SEO, and a robust React ecosystem for dynamic interfaces.

### 5.3 Database and Cache: PostgreSQL and Redis
* **Decision:** PostgreSQL will be the main relational database, and Redis will be used for cache, rate limiting, and messaging.
* **Reason:** PostgreSQL is highly reliable, supports complex transactions, and efficiently handles soft deletes and structured data (JSONB). Redis will be used specifically for:
  * **Paginated Feed Cache:** Store the first pages of the chronological feed in memory to reduce database load.
  * **Basic Rate Limiting:** Protect critical endpoints (e.g., login, upload) against abuse and brute-force attacks.
  * **JWT Token Blacklist:** Store invalidated tokens (logout) until their natural expiration, ensuring security without overloading the relational database.
  * **Future Optimizations:** Serve as a message broker for asynchronous processing (e.g., Celery) in later phases.
* **Benefit:** Guaranteed data integrity, high feed delivery performance, and robust protection against abuse.

### 5.4 Infrastructure: Containerization with Docker
* **Decision:** The entire application (backend, frontend, database, cache) must be containerized using Docker and orchestrated via `docker-compose`.
* **Reason:** Ensure absolute parity between development, staging, and production environments, eliminating the "works on my machine" problem.
* **Benefit:** Easier deployment, simplified horizontal scalability, and dependency isolation.

### 5.5 File Storage: Object Storage (S3) and Environment Parity
* **Decision:** PDF files and profile images will be stored in S3-compatible services (AWS S3, MinIO, etc.), storing only the URL in the database.
* **Environment Parity (Dev vs. Prod):** In local development (Docker), media and PDF uploads must use local volume storage (using Django's `MEDIA_ROOT`). AWS S3 usage must be enabled exclusively in Production and Staging through environment variables, ensuring cost efficiency and ease of offline testing.
* **Reason:** Relational databases are not optimized for storing large blobs. Environment parity avoids unnecessary costs during development and facilitates offline work.
* **Benefit:** Infinite storage scalability in production, possibility of using CDN for fast delivery, and an agile local development environment without mandatory external dependencies.

---

## 6. DevOps, Standards, and Code Quality
To maintain technical excellence and long-term maintainability, the project will adopt rigorous DevOps and code quality practices.

### 6.1 Continuous Integration (CI)
* **Requirement:** Implementing a Continuous Integration (CI) pipeline using GitHub Actions (or similar) is mandatory.
* **Validations:** The CI pipeline must run automatically on every Pull Request (PR) and must block merge if there is failure in:
  * Automated tests (unit and integration).
  * Linters and code formatters (e.g., Flake8/Black for Python, ESLint/Prettier for JavaScript/TypeScript).
  * Database migration validation (ensure there are no conflicts or pending migrations).

### 6.2 Versioning and Commit Standards
* **Conventional Commits:** Strict adoption of the Conventional Commits standard for all commit messages (e.g., `feat: adds PDF upload`, `fix: fixes feed pagination error`, `chore: updates dependencies`, `docs: updates README`).
* **Branching Strategy:** Use of a workflow based on Git Flow or Trunk-Based Development, with protected branches (`main` / `master`) requiring code review before merge.

### 6.3 Code Documentation
* **Professional READMEs:** Maintenance of clear and up-to-date `README.md` files at the root of each repository (frontend and backend), detailing local setup instructions (via Docker), required environment variables, useful commands, and basic architecture.
* **Docstrings and Comments:** Clean and self-explanatory code, with docstrings in complex functions and classes, especially in backend business rules.

---

## 7. Security and Robustness
The platform's academic and institutional nature requires production-grade security from day zero.

### 7.1 Authentication and Session Management
* **Secure JWT in Cookies:** Authentication will be based on JSON Web Tokens (JWT). To ensure maximum security, tokens (Access Token and Refresh Token) must not be stored in `localStorage` or `sessionStorage`. They must travel exclusively through cookies configured with the flags:
  * `HttpOnly`: Prevents cookie access via JavaScript in the frontend.
  * `Secure`: Ensures the cookie is only sent over HTTPS connections.
  * `SameSite=Lax` (or `Strict` for critical routes): Prevents cookie sending in unintended cross-site requests.
* **XSS Prevention and Relation to CSRF:** The use of `HttpOnly` cookies is the main defense against token theft via Cross-Site Scripting (XSS). However, when using cookies for authentication, the application becomes vulnerable to Cross-Site Request Forgery (CSRF). Therefore, CSRF protection becomes mandatory together with this approach.

### 7.2 Strict Upload Validation
* **MIME Type Verification:** The backend must perform strict validation of publication uploads to S3. It is not enough to verify file extension (`.pdf`); verification of the file's real MIME type (must be `application/pdf`) using appropriate libraries (e.g., `python-magic`) is mandatory.
* **Limits and Sanitization:** Enforce size limit (50MB) in both reverse proxy and application.
* **Unique Naming:** To avoid name collisions and overwrite attacks, all uploaded files must be renamed in the backend using UUIDs (e.g., `[uuid].pdf`) before storage in S3. The original name may be stored in database metadata, if necessary.
* **Future Recommendation:** In later phases, integration of a malware scanning service (e.g., ClamAV) in the upload pipeline is recommended, as well as additional validation of the internal PDF structure to prevent malicious script injection.

### 7.3 Protection Against Common Vulnerabilities
* **CSRF (Cross-Site Request Forgery):** Due to the use of cookies for authentication (see 7.1), implementing CSRF protection is mandatory for all mutable requests (POST, PUT, PATCH, DELETE). The frontend (Next.js) must obtain the CSRF token provided by the backend (Django) and include it in the header (e.g., `X-CSRFToken`) of each request that changes server state.
* **IDOR:** Strict authorization validation on all endpoints. The backend must always verify whether the authenticated user has permission to access or modify the requested resource.

### 7.4 Privacy and LGPD Compliance
* **Data Anonymization:** In case of account deletion (Soft Delete), the user's sensitive personal data (PII) must be obfuscated or anonymized in database tables, keeping only UUID for relational integrity. Publications and comments remain under authorship of "Deleted User."
* **Consent:** Clear terms of use and privacy policies, with recorded user consent at registration.

---

## 8. Non-Functional Requirements and Metrics

### 8.1 Performance
* **Feed Loading Time:** Maximum API response time for initial loading and pagination of the chronological feed must be below 1.5 seconds at the 95th percentile (p95).
* **PDF Reading:** Time to start PDF viewing or download (Time to First Byte - TTFB) must be below 1.5 seconds.
* **Asset Optimization:** Profile images and other static assets must be compressed and served through CDN.

### 8.2 Observability
* **Error Tracking:** Mandatory integration with error tracking and performance monitoring tools (e.g., Sentry) in both frontend and backend.
* **Structured Logs and Correlation:** Backend must emit structured logs (JSON format) to facilitate ingestion and analysis by log aggregation tools (e.g., ELK Stack, Datadog). To ensure traceability, all requests must generate a unique `request_id`, which must be propagated across all logs and services involved in that transaction.
* **Traceability of Critical Actions:** Logs must include relevant context (e.g., `user_id`, `request_id`, `endpoint`, `ip_address`) without exposing sensitive data (passwords, tokens). Critical actions (e.g., login, file upload, data deletion) must be explicitly logged with their respective outcomes (success or failure).
* **Audit:** Immutable record of all administrative and moderation actions.

### 8.3 Accessibility
* **WCAG Compliance:** The user interface must comply with WCAG 2.1 Level AA accessibility guidelines.
* **Specific Requirements:**
  * Full support for keyboard navigation (no focus traps).
  * Compatibility with screen readers (correct use of semantic HTML tags and ARIA attributes).
  * Adequate color contrast for text and interactive elements.

### 8.4 Scalability and Availability
* **Stateless:** Backend application must be stateless, allowing horizontal scalability.
* **Availability:** Architecture must be designed to support high availability, with retry mechanisms for temporary network failures (e.g., when communicating with S3 or email services).

---

## 9. Business Rules (In-Depth)

### 9.1 Publication Versioning
* **RN-VER-01:** A publication may have multiple versions. The most recent version is always displayed by default.
* **RN-VER-02:** Previous versions cannot be deleted by the author, ensuring historical traceability.
* **RN-VER-03:** Each new version requires a new PDF upload and a mandatory "Version Notes" field (changelog).
* **RN-VER-04:** Comments made on a previous version remain visible but receive a tag indicating the version in which they were made (e.g., "Comment on v1.1").

### 9.2 Co-authorship
* **RN-COA-01:** The primary author (submitter) can add co-authors by searching existing profiles on the platform.
* **RN-COA-02:** Added co-authors receive a notification and must "Accept" co-authorship for the publication to appear on their profiles.
* **RN-COA-03:** If a co-author rejects, their name is removed from publication metadata in the system (although it may remain in the original PDF).
* **RN-COA-04:** Only the primary author can submit new versions.

### 9.3 Feed and Ordering
* **RN-FED-01:** The default feed is reverse chronological, prioritizing publications and activities (endorsements, comments) from direct connections and followed users.
* **RN-FED-02:** The system must limit pagination to 20 items per request (lazy loading).
* **RN-FED-03:** Feed updates occur via pull-to-refresh or page reload.
* **RN-FED-04:** The feed is not real-time in the MVP. Updates occur exclusively through manual refresh, navigation to another page and return, or through a new paginated call (scroll).

### 9.4 In-app Notifications
* **RN-NOT-01:** The system must keep a notification history for each user, with a maximum retention time of 90 days.
* **RN-NOT-02:** An automated cleanup policy (e.g., via cron job or Celery beat) must physically remove notifications older than 90 days to avoid database bloat.
* **RN-NOT-03:** Notification listing must be paginated (e.g., 20 per page) and ordered from most recent to oldest.
* **RN-NOT-04:** To avoid overload, the notification listing endpoint must have a strict requests-per-minute limit (rate limiting via Redis).

### 9.5 Moderation and Reports
* **RN-MOD-01:** Any authenticated user can report a publication, comment, or profile.
* **RN-MOD-02:** A report temporarily hides the content for the reporter but keeps it visible for others until a moderator review.
* **RN-MOD-03:** If content receives 5 reports from distinct users, it enters automatic quarantine (globally hidden) until review.
* **RN-MOD-04:** Moderators have an internal SLA (Service Level Agreement) of 48 hours to analyze reports.
* **RN-MOD-05:** Moderation actions (hide, warn, suspend) must require a justification recorded in the system (audit and traceability).

**Report Lifecycle and States**
* `pending`: Report received, awaiting triage.
* `under_review`: A moderator has taken ownership of the report and is analyzing it.
* `resolved_action_taken`: Report upheld, punitive/corrective action applied.
* `resolved_no_action`: Report dismissed, no action taken.
* `appealed`: The author of the penalized content appealed the decision.
* `closed`: Process finalized and archived.

---

## 10. Data Model (In-Depth)
The relational database (PostgreSQL) must support the following main entities:

**Entity: `users`**
* `id`: UUID (Primary Key)
* `email`: VARCHAR(255) UNIQUE NOT NULL
* `password_hash`: VARCHAR(255) NOT NULL
* `full_name`: VARCHAR(255) NOT NULL
* `role`: ENUM('member', 'moderator', 'admin') DEFAULT 'member'
* `status`: ENUM('pending', 'active', 'suspended', 'banned') DEFAULT 'pending'
* `created_at`: TIMESTAMP DEFAULT NOW()
* `updated_at`: TIMESTAMP DEFAULT NOW()
* `deleted_at`: TIMESTAMP NULL (Soft Delete)
* *Indexes:* `idx_users_email`, `idx_users_status`

**Entity: `profiles`**
* `user_id`: UUID (Primary Key, Foreign Key -> users.id)
* `bio`: TEXT
* `affiliation`: VARCHAR(255)
* `title`: VARCHAR(100)
* `avatar_url`: VARCHAR(512)
* `deleted_at`: TIMESTAMP NULL (Soft Delete)
* *Indexes:* `idx_profiles_affiliation`

**Entity: `publications`**
* `id`: UUID (Primary Key)
* `author_id`: UUID (Foreign Key -> users.id)
* `title`: VARCHAR(500) NOT NULL
* `abstract`: TEXT NOT NULL
* `doi`: VARCHAR(100) UNIQUE NULL
* `status`: ENUM('draft', 'published', 'hidden') DEFAULT 'published'
* `created_at`: TIMESTAMP DEFAULT NOW()
* `updated_at`: TIMESTAMP DEFAULT NOW()
* `deleted_at`: TIMESTAMP NULL (Soft Delete)
* *Indexes:* `idx_publications_author`, `idx_publications_status`

**Entity: `publication_versions`**
* `id`: UUID (Primary Key)
* `publication_id`: UUID (Foreign Key -> publications.id ON DELETE CASCADE)
* `version_number`: VARCHAR(20) NOT NULL (e.g., 'v1.0')
* `file_url`: VARCHAR(512) NOT NULL
* `changelog`: TEXT
* `created_at`: TIMESTAMP DEFAULT NOW()
* *Indexes:* `idx_versions_publication`

**Entity: `comments`**
* `id`: UUID (Primary Key)
* `publication_id`: UUID (Foreign Key -> publications.id ON DELETE CASCADE)
* `version_id`: UUID (Foreign Key -> publication_versions.id)
* `author_id`: UUID (Foreign Key -> users.id)
* `content`: TEXT NOT NULL
* `parent_id`: UUID NULL (Self-referencing for threads)
* `status`: ENUM('active', 'hidden') DEFAULT 'active'
* `created_at`: TIMESTAMP DEFAULT NOW()
* `deleted_at`: TIMESTAMP NULL (Soft Delete)
* *Indexes:* `idx_comments_publication`

**Entity: `connections`**
* `requester_id`: UUID (Foreign Key -> users.id)
* `receiver_id`: UUID (Foreign Key -> users.id)
* `status`: ENUM('pending', 'accepted', 'rejected') DEFAULT 'pending'
* `created_at`: TIMESTAMP DEFAULT NOW()
* *Primary Key:* (requester_id, receiver_id)

**Entity: `notifications`**
* `id`: UUID (Primary Key)
* `user_id`: UUID (Foreign Key -> users.id ON DELETE CASCADE)
* `type`: ENUM('endorsement', 'comment', 'connection_request', 'system')
* `content`: TEXT NOT NULL
* `is_read`: BOOLEAN DEFAULT FALSE
* `created_at`: TIMESTAMP DEFAULT NOW()
* *Indexes:* `idx_notifications_user_read`

**Entity: `reports`**
* `id`: UUID (Primary Key)
* `reporter_id`: UUID (Foreign Key -> users.id)
* `target_type`: ENUM('publication', 'comment', 'profile')
* `target_id`: UUID NOT NULL
* `reason`: TEXT NOT NULL
* `status`: ENUM('pending', 'under_review', 'resolved_action_taken', 'resolved_no_action', 'appealed', 'closed') DEFAULT 'pending'
* `moderator_id`: UUID NULL (Foreign Key -> users.id)
* `created_at`: TIMESTAMP DEFAULT NOW()
* `updated_at`: TIMESTAMP DEFAULT NOW()

---

## 11. Soft Delete Policy
To ensure referential integrity, academic traceability, and LGPD compliance, the system primarily adopts soft delete.
* **Soft Delete vs Physical Deletion:** Soft Delete is the standard for deletion actions performed by users or moderation. Physical deletion (Hard Delete) is restricted to ephemeral data (e.g., old notifications) or direct administrative intervention.
* **Related Data:** When a user is "deleted" (soft delete), their publications and comments remain in the system to preserve debate context, but authorship is displayed as "Deleted User" (anonymization).
* **LGPD and Anonymization:** A user's soft delete must be accompanied by obfuscation of sensitive data (PII) in the `users` and `profiles` tables, keeping only UUID for relational integrity.

---

## 12. API Conventions
Communication between frontend and backend must follow a rigorous RESTful standard.

* **API Documentation (OpenAPI/Swagger):** The REST API must be rigorously documented using the OpenAPI 3.0 standard. In the Django ecosystem, the `drf-spectacular` library must be used to automatically generate documentation from code and provide an interactive interface (Swagger UI) for route testing in development environments.
* **Versioning Prefix:** All routes must be prefixed with `/api/v1/`.
* **Naming:** Endpoints must use plural nouns and kebab-case (e.g., `/api/v1/publication-versions`).
* **Authentication:** Protected routes require JWT token validation via `HTTP-Only` cookie.
* **Pagination (Cursor Pagination):** Endpoints that return lists (especially publication feed and notifications) must use **Cursor Pagination** (and not offset/page-number pagination). This is essential to avoid duplicated or missing item bugs during frontend infinite scroll in Next.js if new publications are inserted concurrently.
* **Filters and Ordering:** Must use standardized query parameters (e.g., `?sort=-created_at&status=published`).
* **Global Response Pattern:** All API responses must follow a consistent structured format, facilitating frontend error handling.

**Success Example:**
```json
{
  "data": { ... },
  "meta": { "next_cursor": "cD0yMDIzLTEwLTI1VDEwJTNBMzAlM0EwMC4wMDBa", "has_next": true },
  "error": null
}
```

**Error Example:**
```json
{
  "data": null,
  "meta": null,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "The provided data is invalid.",
    "details": { "email": ["This field is required."] }
  }
}
```

Common error codes must include: `VALIDATION_ERROR` (400), `AUTHENTICATION_ERROR` (401), `AUTHORIZATION_ERROR` (403), `NOT_FOUND` (404), and `INTERNAL_SERVER_ERROR` (500).

---

## 13. Testing Strategy
Quality will be ensured through a pragmatic testing pyramid:
* **Unit Tests:** Focused on critical backend business rules (e.g., password validation, statistics calculations, versioning logic).
* **Integration Tests:** Validation of API endpoints, especially file upload flows (S3) and database interactions.
* **Permission and Security Tests:** Automated tests to ensure regular users cannot access moderation routes and visitors cannot download PDFs.
* **Acceptance Tests (E2E):** Automation of critical flows (Registration -> Approval -> Publication -> Comment) using tools such as Cypress or Playwright.

---

## 14. MVP Definition of Done Criteria
The Minimum Viable Product will be considered "Ready for Launch" when:
1. The end-to-end flow (Registration -> Approval -> Publication -> Reading -> Comment) can be executed without critical errors.
2. PDF upload and download are functioning securely and performantly, with strict MIME type validation.
3. The moderation panel is operational for managing onboarding of new users and basic reports.
4. The interface is responsive, accessible (WCAG 2.1 AA), and visually aligned with prototypes.
5. The CI/CD pipeline is configured and blocking PRs with test or linter failures.
6. Performance metrics (loading time < 1.5s) are being met.
7. No "High" or "Critical" severity bug is open in the backlog.

---

## 15. Final Considerations
The Histora project presents a clear and necessary value proposition for the community of historians of education. The scope defined in this DRS balances conceptual ambition with the need for a robust, secure, and scalable architecture. Adopting rigorous DevOps, security, and code quality practices from the beginning ensures that the platform is born with its academic identity preserved and prepared for future growth.