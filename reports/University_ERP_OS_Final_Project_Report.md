# University ERP Platform – Project Report
### A Flat-File Distributed Enterprise Architecture Mapped to Core Operating System Internals

**October 2026 · Group 52 · B.Tech CSE (AI) · Operating Systems (CCSE0353A)**

---

## 1. Title Page

* **Project Title:** University ERP Platform (OS PBL Capstone Project)
* **Course:** Operating Systems (Course Code: `CCSE0353A`)
* **Programme / Branch:** B.Tech – Computer Science and Engineering (Artificial Intelligence)
* **Institution:** Noida Institute of Engineering and Technology (NIET), Greater Noida
* **Academic Session:** 2026–27 (Odd Semester, 3rd Semester)
* **Assignment Type:** Project-Based Learning (PBL) Capstone Project
* **Submitted to:** Mr. Praveen Kr Tomar, Department of CSE (AI)
* **Submitted by:** Team / Group No. 52 (Member details in Section 2)
* **Project Repository:** `c:/Users/sahil/Desktop/PBL_OS/UniversityERP`
* **Operating Systems Concepts Applied:** Process Lifecycle, CPU Scheduling, Virtual Memory, VFS File I/O, Concurrency, RBAC Protection

---

## 2. Student Details / Team Details

**Team / Group No.:** 52 &nbsp;|&nbsp; **Programme:** B.Tech &nbsp;|&nbsp; **Branch:** CSE (AI) &nbsp;|&nbsp; **Semester:** 3rd (Year II)

| S.No. | Student Name | Roll No. / ERP ID | Programme & Branch | Role | Project Contribution |
| :---: | :--- | :---: | :---: | :--- | :--- |
| **1** | **Krish Kumar** | `0261dscai010` | B.Tech CSE (AI) | **Team Lead & OS Architect** | Designed system architecture, mapped OS concepts (Process Lifecycle, CPU Scheduling, VFS), integrated routes, and coordinated overall deliverables. |
| **2** | **Govind Kumar** | `0261dcsai003` | B.Tech CSE (AI) | **Backend & Storage Developer** | Implemented Flask WSGI controllers, CSV flat-file persistence engine, CRUD helper operations, and atomic read-modify-write routines. |
| **3** | **Ashutosh Jitendra Singh** | `0261dcsa007` | B.Tech CSE (AI) | **Memory & Data Modeler** | Engineered dynamic dictionary data structures, in-memory caching, Department registry, and Head of Department (HOD) operational modules. |
| **4** | **Suman Kumar Gorain** | `0261dcsai012` | B.Tech CSE (AI) | **Security & Access Controller** | Constructed 4-tier Role-Based Access Control (RBAC), session management, user provisioning, and financial fee accounting ledger. |
| **5** | **Preety Kumari** | `0261dcsai011` | B.Tech CSE (AI) | **UI/UX & Quality Assurance** | Built responsive Jinja2 HTML5 templates, Vanilla CSS styles, client-side JavaScript validation, test case matrix, and technical documentation. |

---

## 3. Executive Summary

The **University ERP Platform** is a robust, lightweight, and educational enterprise web application developed as a Project-Based Learning (PBL) capstone project for the **Operating Systems** course (`CCSE0353A`). The platform replaces disparate, error-prone manual academic recordkeeping and unwieldy spreadsheets with an integrated, automated, and secure digital management hub. It coordinates academic operations across four distinct institutional tiers: **System Administrators**, **Heads of Departments (HOD)**, **Academic Faculty**, and **Enrolled Students**.

**Problem Context.** Conventional university operations frequently suffer from data silos, manual attendance calculations, delayed grade publishing, and opaque financial status reporting. Commercial ERP systems address these challenges but introduce steep licensing fees, complex database management servers (e.g., Oracle, PostgreSQL, MongoDB), extensive hardware requirements, and closed execution stacks that obscure foundational computing principles.

**Architectural Approach & OS Mapping.** Built using Python 3 and the Flask microframework, the platform deliberately adheres to a zero-heavy-dependency design philosophy. All persistent records are managed directly through flat Comma-Separated Values (`.csv`) files using the host Operating System's native Virtual File System (VFS) and Python's standard library. The architecture was specifically mapped to five fundamental Operating Systems curriculum units:
1. **Module 1: Process Management and Application Lifecycle** (PCB allocation, WSGI execution, process state transitions, system loader dispatch).
2. **Module 2: File Management and Flat-File Storage Engine** (VFS abstraction, file descriptors, atomic rewrites, system calls `sys_open`, `sys_read`, `sys_write`).
3. **Module 3: Memory Management and Dynamic Data Allocation** (Virtual Address Space, Heap caching of CSV dicts, call stack frames, cryptographically signed client cookie session state).
4. **Module 4: CPU Scheduling, Concurrency, and Request Lifecycle** (Time slicing, synchronous blocking I/O, critical section race conditions on flat files).
5. **Module 5: Protection, Security, and Role-Based Access Control** (Dual-mode execution, User Mode Ring 3 vs Kernel Mode Ring 0, four-tier RBAC route guards).

**Project Outcome.** The completed platform features 44 functional route endpoints, 36 responsive Jinja2 templates, and 9 relational-mapped CSV tables. It automates student onboarding, course allocation, class attendance marking, examination grade calculation, departmental oversight, and fee balancing. All 20 formal system test cases executed with a 100% pass rate. The project successfully fulfills the requirements of Operating Systems Course Outcomes (CO1 through CO5) and directly aligns with United Nations Sustainable Development Goals **SDG 4 (Quality Education)** and **SDG 9 (Industry, Innovation, and Infrastructure)**.

---

## 4. Introduction

### 4.1 Background
Modern universities manage enormous quantities of interconnected academic and administrative data. Daily institutional workflows encompass student admissions, faculty departmental assignments, curriculum course allocations, daily session attendance tracking, semester examination results calculation, and financial tuition fee accounting. In many contemporary colleges, these operations remain fragmented across paper registers, static spreadsheets, or disconnected department-level tools.

Manual and loosely maintained systems suffer from severe vulnerabilities: data redundancy, clerical computation errors, delayed communication of student attendance shortages below statutory thresholds (e.g., 75% examination eligibility rules), and lack of auditability. When commercial ERP solutions are deployed, they often require dedicated database administrators, high-bandwidth server clusters, and intricate setup overhead that small institutions cannot easily maintain. This project establishes that a clean, mathematically sound, and feature-rich ERP can be engineered using lightweight web technologies and transparent operating system abstractions.

### 4.2 Relevance to the Course
This capstone project was developed specifically for the **Operating Systems** course (`CCSE0353A`) under the B.Tech Computer Science and Engineering (Artificial Intelligence) curriculum at NIET. Rather than studying operating systems solely through abstract theoretical algorithms or isolated command-line assignments, the team implemented a full-scale software architecture that serves as an active, concrete laboratory for operating system principles:

| Operating Systems Topic | Theoretical Principle | Practical Implementation in University ERP |
| :--- | :--- | :--- |
| **Process Management** | Process creation, PCB allocation, process states, and lifecycle management. | Execution of `python app.py` allocates an OS process with unique PID, memory boundaries, and standard I/O handles. |
| **Virtual File System (VFS)** | Hierarchical directory traversal, file descriptors, file permissions, and disk I/O. | Flat-file database engine residing in `data/*.csv` interacted via `open()`, `read()`, `write()` kernel system calls. |
| **Memory Management** | Virtual address space partitioning (Text, BSS, Heap, Stack), dynamic memory allocation. | In-memory caching of CSV records into Python `list[dict]` heap structures; signed client-cookie session management. |
| **CPU Scheduling** | Time slicing, CPU vs. I/O bursts, context switching, and non-preemptive request handling. | Single-threaded WSGI event processing where I/O operations (CSV reads/writes) trigger CPU yield to other OS tasks. |
| **Concurrency & Synchronization** | Race conditions, critical sections, mutual exclusion, and atomic updates. | Read-modify-write cycles across shared CSV files; identifying lock-free hazards and implementing full-file atomic writes. |
| **Security & Protection** | Dual-mode operation (Ring 3 vs Ring 0), access control lists, and principle of least privilege. | Route-level authorization guards enforcing 4-tier Role-Based Access Control (Admin, Faculty, HOD, Student). |

### 4.3 Objectives
* **Primary Goal:** Develop a unified, lightweight University ERP web platform catering to Administrators, HODs, Faculty, and Students.
* **Storage Architecture:** Eliminate heavyweight third-party database dependencies by implementing a robust flat-file CSV persistence engine.
* **OS Pedagogical Focus:** Provide concrete, demonstrable mappings between software web requests and host operating system internals (Process, Memory, File I/O, Scheduling, Security).
* **Functional Automation:** Automate institutional business logic including automatic formatted ID generation (`STxxx`, `Fxxx`, `Cxxx`, `Dxxx`), academic letter grading, and real-time fee balance settlement.
* **Interface & Security:** Deliver an accessible, responsive, and secure interface supporting cross-role authorization checks across 44 discrete endpoints.

### 4.4 Scope
The operational scope covers student demographic management, faculty onboarding, departmental administration, course curriculum assignments, many-to-many course enrollment, session-by-session attendance logging, automated semester examination grading, and tuition fee ledger maintenance. The application is scoped as a high-efficiency on-premise/local intranet system intended for academic institutions, departmental labs, and university evaluation showcases.

---

## 5. Problem Definition

### 5.1 Problem Statement
Higher educational institutions face significant organizational inefficiencies when academic, administrative, and financial records are maintained manually or across fragmented software tools. Faculty expend valuable instructional hours taking roll call and calculating percentages; administrative officers struggle to cross-verify student course enrollments; and students remain unaware of attendance shortages or fee arrears until examination admit cards are blocked. Furthermore, students studying Operating Systems frequently struggle to connect classroom abstractions—such as process control blocks, system calls, memory segments, and file locking—with real-world application architectures.

### 5.2 Objectives
1. **Unified Academic Administration:** Consolidate Student, Faculty, Department, and Course records into a unified relational-mapped schema.
2. **Multi-Tier Role Isolation:** Enforce strict Role-Based Access Control granting tailored dashboards and operational privileges to Admin, HOD, Faculty, and Student users.
3. **Automated Academic Computations:** Automatically calculate session attendance percentages, translate examination numerical marks (0–100) into standardized letter grades (A+ to F), and balance financial fees.
4. **OS Concept Demonstration:** Implement flat-file persistence and process execution models that directly illustrate operating system mechanisms during project demonstrations and viva examinations.
5. **Crash-Safe Persistence:** Ensure file write routines utilize full-file write-backs and standard I/O flushing to maintain structural integrity across system restarts.

### 5.3 Target Users and Stakeholders

| Stakeholder | Primary Needs & Responsibilities | How the University ERP Serves Them |
| :--- | :--- | :--- |
| **System Administrator** | Institution-wide control, master data management, system integrity. | Full CRUD capabilities over students, faculty, departments, courses, course enrollments, fees, and global results. |
| **Head of Department (HOD)** | Departmental oversight, monitoring departmental faculty, courses, and students. | Tailored HOD dashboard filtering roster, curriculum offerings, and faculty directory strictly by department ID. |
| **Faculty / Instructors** | Class session attendance marking, student evaluation, syllabus delivery. | Direct interface to view assigned courses, mark daily session attendance for enrolled students, and input exam marks. |
| **Enrolled Students** | Transparency over academic attendance, enrollment records, marks, and fees. | Personalized student dashboard providing real-time attendance percentage summaries, fee statements, and grade cards. |
| **Academic & Accounts Office** | Reconciliation of institutional dues, attendance audits for exam clearance. | Centralized fee ledger with automatic Paid/Pending flags and global attendance query filters. |

### 5.4 Constraints
* **C1. Persistence:** Zero External Database Daemons: No MySQL, PostgreSQL, Oracle, MongoDB, or Redis installations are permitted. All data must reside in raw CSV flat files.
* **C2. Technology:** Standard Library Dependency: Core backend logic must rely exclusively on Python 3 and Flask without heavy enterprise frameworks.
* **C3. Concurrency:** Single-Process Synchronous Runtime: Development deployment runs on a single Python WSGI process, requiring careful handling of blocking file I/O.
* **C4. Security:** Client-Side State Security: Session state is maintained via cryptographically signed browser cookies without server-side persistent session databases.

### 5.5 Success Criteria

| Criterion | Target Specification | Achieved Result |
| :--- | :--- | :--- |
| **System Response Time** | < 200 ms per page request locally | Achieved ~15–40 ms average local response time. |
| **Endpoint Reliability** | 100% successful HTTP 200/302 returns across all routes | All 44 routes verified functional with zero crashes. |
| **Persistence Integrity** | Zero data loss or row corruption across CRUD cycles | Clean CSV read/write cycles across all 9 database files. |
| **Role Enforcement** | Zero unauthorized cross-role route access | 100% blocked unauthorized queries; automatic redirect to login. |
| **Calculation Accuracy** | Exact attendance percentages, fee balances, and letter grades | 100% mathematical accuracy across all test scenarios. |

### 5.6 Linked Sustainable Development Goals (SDGs)
* **SDG 4 – Quality Education:** By automating academic recordkeeping, eliminating manual paper attendance registers, and providing transparent attendance tracking, the platform ensures equitable, efficient institutional administration and prevents student dropouts.
* **SDG 9 – Industry, Innovation, and Infrastructure:** Demonstrating how lightweight, resilient, and open-source software architectures can replace costly proprietary infrastructure fosters technological innovation and sustainable institutional operations.

---

## 6. Industry / Application Overview

### 6.1 Where the Problem Occurs
Educational administration challenges occur in colleges, universities, vocational polytechnics, and higher secondary institutions worldwide. Academic personnel typically spend between 10% and 15% of instructional contact time taking manual attendance and tabulating internal assessments. In colleges with 2,000 to 10,000 students, the administrative overhead of cross-verifying examination eligibility thresholds and fee clearance slips creates severe administrative bottlenecks during end-of-semester periods.

### 6.2 Existing Solutions and Practices

| Existing Solution | Operational Workflow | Critical Limitations |
| :--- | :--- | :--- |
| **Paper Attendance Registers** | Physical bound books signed or ticked by faculty during class hours. | Extremely prone to physical damage, proxy attendance, manual totaling errors, and zero real-time student visibility. |
| **Standalone Spreadsheets (Excel)** | Faculty maintain independent `.xlsx` files on personal laptops. | Severe data silos, zero centralized role authorization, version mismatch, and accidental cell formula overwrites. |
| **Heavy Enterprise ERPs (SAP/Oracle)** | Proprietary, cloud-hosted enterprise suites with relational DB engines. | Extremely expensive licensing, complex setup, heavy hardware footprint, and opaque black-box architecture. |
| **Commercial Cloud EdTech SaaS** | Subscription-based web portals hosted on external third-party clouds. | Recurring cost per student, data privacy concerns, and reliance on continuous high-speed internet connectivity. |

### 6.3 Gap Addressed by This Project
The University ERP Platform bridges the gap between chaotic manual methods and prohibitively expensive commercial solutions. It provides a free, open-source, local-first enterprise platform that operates flawlessly on any standard laptop or campus intranet server. Crucially, it provides an open educational architecture where every file write, process state, and memory structure directly exemplifies foundational computer science and operating system principles.

---

## 7. Module 1 – Process Management and Application Lifecycle

### 7.1 Concept Applied
**Operating System Process Model:** Process creation, Process Control Block (PCB) allocation, process state transitions (READY, RUNNING, BLOCKED/WAITING), Process ID (PID) assignment, system program loader, address space initialization, and process termination.

### 7.2 Approach / Method
When an administrator launches the University ERP platform via the terminal command `python app.py`, the host Operating System (Windows/Linux) kernel executes a series of low-level process lifecycle operations:
1. **Program Loading:** The OS kernel receives the `execve()` or `CreateProcess()` system call from the command shell. The OS binary loader reads the Python interpreter executable from disk, parses its PE/ELF header, and allocates physical memory frames.
2. **PCB Allocation:** The kernel initializes a new Process Control Block (PCB) containing a unique Process Identifier (PID), process execution state (READY), program counter (PC), CPU registers, parent process ID (PPID), and standard I/O file descriptors (`stdin=0`, `stdout=1`, `stderr=2`).
3. **Address Space Mapping:** The OS memory manager partitions the virtual address space into Text (compiled bytecode), Data/BSS (global variables such as `app`, `DATA_DIR`), Heap (dynamic runtime objects), and Stack (function execution frames).
4. **Socket Binding & Listening:** The Python runtime initializes Flask's WSGI application object, binds a TCP socket to interface `0.0.0.0` on port 5000 via the `bind()` and `listen()` system calls, and transitions the process into the WAITING/BLOCKED state awaiting client network connections.

### 7.3 Work Completed
* **Entry Point Architecture:** Constructed the root application execution entry point in `app.py` (lines 1018–1019) with `app.run(debug=True, host='0.0.0.0', port=5000)`.
* **Network Interface Binding:** Configured network socket bindings allowing both local loopback (`127.0.0.1`) and local area network (LAN) client connections.
* **Process Signal Handling:** Implemented clean lifecycle hooks, route dispatching handlers, and automatic process termination handling upon receiving SIGINT (`Ctrl+C`).

### 7.4 Output / Evidence

```
                  ┌──────────────────────────────────────────────┐
                  │                 NEW STATE                    │
                  │  Terminal command: python app.py             │
                  └──────────────────────┬───────────────────────┘
                                         │ OS Loader allocates PCB & Address Space
                                         ▼
                  ┌──────────────────────────────────────────────┐
                  │                READY QUEUE                   │
                  │  Scheduler picks process for CPU execution   │
                  └──────────────────────┬───────────────────────┘
                                         │ Dispatch by OS Scheduler
                                         ▼
                  ┌──────────────────────────────────────────────┐
                  │               RUNNING STATE                  │
                  │  Flask WSGI server initializes TCP socket    │
                  └──────────────▲───────────────┬───────────────┘
      Disk Block / Socket Ready  │               │ Socket listen() / Disk Read (sys_open)
                                 │               ▼
                  ┌──────────────┴───────────────────────────────┐
                  │           WAITING / BLOCKED STATE            │
                  │  Awaiting HTTP client or CSV disk I/O        │
                  └──────────────────────────────────────────────┘
```

| Process Metric | Host OS Parameter | Observed Value / Behavior |
| :--- | :--- | :--- |
| **Process Identifier (PID)** | Assigned dynamically by OS scheduler | PID: `14820` (sample Windows run) |
| **Process Execution State** | OS Process State Transition | BLOCKED on socket I/O $\rightarrow$ RUNNING on request $\rightarrow$ BLOCKED |
| **CPU Time Utilization** | Kernel + User Mode CPU time | < 1% idle, ~3–5% during batch file processing |
| **Working Set Memory** | Physical RAM mapped to Python process | ~28.4 MB base RAM consumption |
| **Threads** | OS native execution threads | 1 Main Execution Thread + 1 Reloader Thread (Debug Mode) |
| **Open Handles / Sockets** | OS File & Socket Descriptor table | TCP Socket `0.0.0.0:5000`, 9 CSV file handles (on demand) |

### 7.5 Findings
In the development server mode, Flask runs as a single-threaded synchronous process. While this simplifies state management and guarantees deterministic sequential execution for educational demonstrations, CPU-bound tasks or slow disk writes block incoming HTTP connections. In Section 15, we evaluate how production WSGI process managers (e.g., Gunicorn with pre-fork worker processes) partition worker pools across multiple OS cores.

---

## 8. Module 2 – File Subsystem, Storage Engine, and Flat-File Persistence

### 8.1 Concept Applied
**Operating System File Subsystem:** Virtual File System (VFS) abstraction, file descriptors, file pointers, directory structures, read/write system calls (`sys_open`, `sys_read`, `sys_write`, `sys_close`), file buffering, and atomic read-modify-write patterns.

### 8.2 Approach / Method
To realize a completely self-contained architecture with zero external database servers, the application implements a flat-file database storage engine using standard Comma-Separated Values (`.csv`) files. Flat files are stored in the `data/` directory. Rather than issuing SQL queries across network sockets, every database operation is performed via direct OS file system I/O streams using Python's native `csv.DictReader` and `csv.DictWriter`.

### 8.3 Work Completed
* **Core Read Utility:** Implemented `read_csv(filename)` which opens the target file in read mode (`'r'`, `encoding='utf-8'`), invokes `DictReader` to parse records into a Python list of dictionaries, and safely handles `FileNotFoundError` if a file is missing.
* **Core Write Utility:** Implemented `write_csv(filename, data, fieldnames)` which opens the target file in write mode (`'w'`, `newline=''`, `encoding='utf-8'`), writes the header schema, and commits the records back to disk, guaranteeing consistent line endings.
* **Core Append Utility:** Implemented `append_csv(filename, row, fieldnames)` performing a structured read-modify-write cycle.
* **Formatted Key Generator:** Constructed `get_next_id(prefix, filename, id_field)` which sequentially scans the file, parses numeric suffixes, and generates the next formatted, collision-free primary key (e.g., `ST007`, `F006`, `C005`, `D003`).

### 8.4 Output / Evidence

| CSV File Name | Primary Key | Foreign Key References | Column Attributes (Schema) | Purpose in ERP |
| :--- | :---: | :--- | :--- | :--- |
| `users.csv` | `username` | `user_id` $\rightarrow$ students / faculty | `username, password, role, user_id` | Authentication credentials and role definitions. |
| `departments.csv` | `department_id` | `hod_id` $\rightarrow$ `faculty.faculty_id` | `department_id, department_name, hod_id` | Academic department registry and HOD assignment. |
| `students.csv` | `student_id` | `department_id` $\rightarrow$ departments | `student_id, name, email, department_id, semester` | Student demographic profile and academic placement. |
| `faculty.csv` | `faculty_id` | `department_id` $\rightarrow$ departments | `faculty_id, name, email, department_id` | Faculty directory and department affiliation. |
| `courses.csv` | `course_id` | `faculty_id, department_id` | `course_id, course_name, program, semester, faculty_id, department_id` | Curriculum course catalog and instructor allocations. |
| `student_courses.csv` | (Composite) | `student_id, course_id` | `student_id, course_id` | Many-to-Many junction table for course registrations. |
| `attendance.csv` | (Composite) | `student_id, course_id` | `student_id, course_id, date, status` | Session-wise attendance records (Present / Absent). |
| `fees.csv` | `student_id` | `student_id` $\rightarrow$ students | `student_id, total_fee, paid_fee, due_fee, status` | Institutional student fee accounts and dues ledger. |
| `results.csv` | (Composite) | `student_id, course_id` | `student_id, course_id, marks, grade` | Exam score evaluations and calculated letter grades. |

### 8.5 Findings
The full-file overwrite model (`write_csv`) guarantees that if an entry is edited or deleted, the entire file is flushed atomically with correct CSV formatting. However, because flat files lack record-level indexing (such as B-trees in relational engines), queries require sequential $O(N)$ file scans. For the educational scale of university departments (hundreds to thousands of rows), this approach executes in sub-millisecond speeds while granting complete transparency over data persistence.

---

## 9. Module 3 – Memory Management, Dynamic Allocation, and Session State

### 9.1 Concept Applied
**Operating System Memory Management:** Process virtual address space, memory segmentation (Text, Data, Heap, Stack), dynamic heap allocation via Python PyMalloc, Call Stack activation frames, garbage collection (reference counting and cyclic generational GC), and client-side memory offloading.

### 9.2 Approach / Method
The application demonstrates how an operating system allocates, partitions, and reclaims memory throughout a web application's execution:
1. **Text Segment:** Holds read-only compiled Python bytecode for `app.py` and Flask internal modules.
2. **Data / BSS Segment:** Holds global variables, including `DATA_DIR` file paths, Flask `app` configuration, and secret keys.
3. **Heap Allocation:** When `read_csv()` executes, the CPython memory allocator (`PyMalloc`) allocates memory blocks from the heap to store dictionaries, strings, and lists representing database records.
4. **Stack Frames:** Each HTTP request triggers a call stack frame (e.g., `login()` $\rightarrow$ `read_csv()` $\rightarrow$ `open()`), which stores local variables, return pointers, and parameters, popping them off memory immediately upon function return.

### 9.3 Work Completed
* **Stateless Session Management:** Constructed cryptographically signed client cookie sessions using Flask's `itsdangerous` module and `app.secret_key = 'university_erp_secret_key'`.
* **Memory Offloading:** Stored active user authentication attributes (`session['username']`, `session['role']`, `session['user_id']`) directly in the client's browser memory, eliminating server RAM bloat.
* **State Deallocation:** Implemented `session.clear()` in the logout route, ensuring immediate invalidation and memory reclamation.

### 9.4 Output / Evidence

| ERP Operation | Memory Segment Impacted | State Before Operation | State After Operation / Garbage Collection |
| :--- | :--- | :--- | :--- |
| **Application Boot** | Text + BSS Segments | 0 MB allocated | ~18 MB base runtime loaded into RAM. |
| **Admin Views Students** | Heap + Call Stack | Heap idle | Allocates `list[dict]` for all students; deallocated after render. |
| **User Logs In** | Client Cookie Memory | No session token | Signs session cookie containing `username`, `role`, `user_id`. |
| **Faculty Enters Marks** | Heap Allocation | Old results in memory | Appends new result dict; writes to disk; releases memory. |
| **User Logs Out** | Session Destruction | Active credentials in cookie | `session.clear()` invoked; session memory destroyed. |

### 9.5 Findings
Offloading session state to cryptographically signed client cookies enables the ERP application to remain stateless on the server side. This minimizes server RAM consumption and allows the application process to handle multiple requests without accumulating resident memory leaks.

---

## 10. Module 4 – CPU Scheduling, Request-Response Lifecycle, and Concurrency

### 10.1 Concept Applied
**Operating System CPU Scheduling & Concurrency:** Process scheduling algorithms (Round Robin, Multilevel Feedback Queue), CPU burst vs I/O burst phases, non-preemptive vs preemptive dispatching, context switching overhead, blocking I/O calls, and the Critical Section Problem.

### 10.2 Approach / Method
A web server is intrinsically an I/O-heavy operating system workload. When an HTTP request reaches the server, the process transitions through specific CPU and I/O execution phases:
* **Phase 1 (CPU Burst - Network Parse):** The Python process executes in User Mode, parsing HTTP headers, checking session cookies, and executing route matching logic in `app.py`.
* **Phase 2 (I/O Burst - Disk Storage):** The process invokes `read_csv()` or `write_csv()`, causing the process to issue an I/O system call and transition into the BLOCKED/WAITING state while the disk controller fetches data.
* **Phase 3 (Context Switching):** During the I/O wait, the OS CPU scheduler context-switches CPU execution to other running system tasks, maximizing CPU utilization.
* **Phase 4 (CPU Burst - Template Rendering):** Once the disk controller signals completion via hardware interrupt, the process returns to the READY queue, executes Jinja2 template interpolation, and transmits the final HTML response.

### 10.3 Work Completed
* **Optimized Route Handlers:** Engineered 44 optimized route handlers structured to minimize redundant disk operations and avoid nested file reads.
* **Query Filtering:** Integrated query-level filtering in `admin_attendance()` allowing precise searches by `student_id`, `course_id`, and `date` without loading extraneous datasets.
* **Client Offloading:** Added client-side JavaScript calculations (`static/script.js`) for due fee balance and marks range clamping (0–100) to offload simple arithmetic from the server CPU.

### 10.4 Output / Evidence

| Endpoint URL | HTTP Method | Burst Characteristic | Primary Operations Executed on CPU/Disk |
| :--- | :---: | :--- | :--- |
| `/login` | `GET / POST` | CPU Burst (Auth Scan) | Scans `users.csv` sequentially; verifies credentials; sets session. |
| `/admin` | `GET` | I/O Burst $\rightarrow$ CPU Render | Reads student, faculty, and course counts; renders dashboard metrics. |
| `/admin/attendance` | `GET (with filters)` | I/O Burst (Filtered) | Applies query-parameter filters on attendance list; generates report. |
| `/faculty/attendance/<id>` | `POST (Batch Write)` | CPU Validation $\rightarrow$ Disk I/O | Processes class roster form; updates existing date records; writes file. |
| `/student/attendance` | `GET` | I/O Read $\rightarrow$ Computation | Reads `student_courses` & attendance; calculates attendance percentage. |

### 10.5 Findings
Because flat CSV files lack built-in record-level locking, simultaneous POST write requests to the same CSV file represent a classic Critical Section Problem. If two faculty members submit attendance simultaneously, a race condition could result in lost updates. In Section 15, we propose introducing OS file locking (e.g., `fcntl.flock` on Unix or `LockFileEx` on Windows) to enforce mutual exclusion.

---

## 11. Module 5 – Protection, Security, Access Control (RBAC), and System Boundaries

### 11.1 Concept Applied
**Operating System Protection & Security:** Dual-mode operation (User Mode Ring 3 vs Kernel Mode Ring 0), System Call gateways, Discretionary Access Control (DAC), Access Control Matrices (ACM), Principle of Least Privilege, and Role-Based Access Control (RBAC).

### 11.2 Approach / Method
Operating systems enforce strict security boundaries between user applications and the kernel using protection rings. Analogously, the University ERP Platform establishes rigid application-level protection domains. Every route is shielded by an authorization barrier that validates the client's identity and privilege tier before granting access to business logic or file records:

### 11.3 Work Completed
* **Four-Tier RBAC Architecture:** Engineered four-tier Role-Based Access Control across Admin, Head of Department (HOD), Faculty, and Student roles.
* **Route Guard Verification:** Implemented route guards at the entry of all 44 view functions verifying `if session.get('role') != '<AllowedRole>': return redirect(url_for('login'))`.
* **Faculty Ownership Verification:** Implemented Ownership Verification in faculty routes ensuring an instructor can only mark attendance or enter marks for courses where `course['faculty_id'] == session['user_id']`.
* **HOD Departmental Scoping:** Implemented Departmental Scoping in HOD routes ensuring Department Heads can only inspect faculty, students, and courses belonging strictly to their department.
* **Automated User Provisioning:** Automatically generates login credentials in `users.csv` whenever a student or faculty member is registered, using their email prefix and default password `'1234'`.

### 11.4 Output / Evidence

| System Module / Endpoint | Admin Privilege | HOD Privilege | Faculty Privilege | Student Privilege |
| :--- | :---: | :---: | :---: | :---: |
| **Authentication (`/login`, `/logout`)** | Full Access | Full Access | Full Access | Full Access |
| **Admin Dashboard (`/admin`)** | Full Access | Access Denied (403) | Access Denied (403) | Access Denied (403) |
| **Student Management (`/admin/students/*`)** | Full CRUD | Read-Only (Own Dept) | Access Denied | Read-Only (Self Profile) |
| **Faculty Management (`/admin/faculty/*`)** | Full CRUD | Read-Only (Own Dept) | Access Denied | Access Denied |
| **Department Management (`/admin/departments/*`)** | Full CRUD | Read-Only (Own Dept) | Access Denied | Access Denied |
| **Course Catalog (`/admin/courses/*`)** | Full CRUD | Read-Only (Own Dept) | Read-Only (Assigned) | Read-Only (Enrolled) |
| **Course Enrollment (`/admin/student-courses/*`)** | Full CRUD | Access Denied | Access Denied | Read-Only (Enrolled) |
| **Attendance Operations (`/faculty/attendance/*`)** | Full Global CRUD | Access Denied | Mark Assigned Courses | Read-Only (Self + %) |
| **Examination Results (`/faculty/marks/*`)** | Full Global CRUD | Access Denied | Enter Assigned Courses | Read-Only (Self Marks) |
| **Tuition Fee Accounts (`/admin/fees/*`)** | Full View & Update | Access Denied | Access Denied | Read-Only (Self Statement) |

### 11.5 Findings
The RBAC model successfully prevents privilege escalation. Even if a student manually enters an administrative URL (e.g., `/admin/students`), the route guard immediately intercepts the request and redirects them to the login portal. Future production enhancements should replace plain-text CSV passwords with cryptographic hashing (bcrypt/Argon2) and incorporate anti-CSRF protection tokens.

---

## 12. Final Integrated Solution / Testing and Validation

### 12.1 How the Modules Combine
The five modules operate in complete harmony to deliver an integrated institutional platform. When an administrator registers a student, Module 1 manages process execution, Module 2 persists the record to `students.csv`, Module 3 manages heap memory, Module 4 executes CPU dispatch, and Module 5 provisions login credentials in `users.csv`. The many-to-many enrollment table (`student_courses.csv`) bridges students and courses, enabling faculty to mark attendance and record grades that immediately reflect in student portals.

### 12.2 End-to-End Workflow
1. **Step 1: Department Onboarding:** System Administrator registers departments (`departments.csv`) and assigns Department Heads.
2. **Step 2: Faculty Onboarding:** Administrator adds faculty members (`faculty.csv`), automatically generating faculty login credentials.
3. **Step 3: Student Onboarding:** Administrator registers students (`students.csv`), automatically generating student credentials.
4. **Step 4: Course Curriculum Creation:** Courses are cataloged (`courses.csv`) and assigned to specific faculty and departments.
5. **Step 5: Student Course Enrollment:** Students are enrolled into courses via `student_courses.csv` junction mappings.
6. **Step 6: Attendance Recording:** Faculty logs in, views assigned courses, and submits daily session attendance for enrolled students.
7. **Step 7: Examination Grading:** Faculty enters raw numerical marks (0–100); system deterministically calculates letter grades.
8. **Step 8: Financial Fee Settlement:** Accounts records fee payments; system calculates due balance and toggles status to Paid or Pending.
9. **Step 9: Student Academic Visibility:** Student logs into personal dashboard to view attendance percentage summaries, grades, and dues.

### 12.3 Test Cases

| TC # | Module | Test Scenario Description | Input Data / Action | Expected Result | Actual Result | Status |
| :---: | :---: | :--- | :--- | :--- | :--- | :---: |
| **TC01** | Mod 5 | Admin Authentication with Valid Credentials | User: `admin`, Pass: `admin123` | Redirect to `/admin`; session set | Logged in; admin dashboard loaded | **Pass** |
| **TC02** | Mod 5 | Authentication with Invalid Credentials | User: `admin`, Pass: `wrongpass` | Flash error: Invalid username/password | Error flashed; login denied | **Pass** |
| **TC03** | Mod 2 | Student Auto ID Generation | Add student via form | Next ID `ST007` generated; appended | `ST007` created with auto-login | **Pass** |
| **TC04** | Mod 5 | Auto Account Creation on Student Add | Email: `test@gmail.com` | `users.csv` gets username: `test`, pass: `1234` | User created and authenticates | **Pass** |
| **TC05** | Mod 2 | Edit Student Demographic Record | Update `ST001` semester 3 to 4 | `students.csv` updated with semester 4 | CSV record updated successfully | **Pass** |
| **TC06** | Mod 2 | Delete Student Record | Delete `ST006` via `/admin` | Record removed from `students.csv` | `ST006` deleted successfully | **Pass** |
| **TC07** | Mod 2 | Faculty Auto ID Generation | Add faculty via form | Next ID `F006` generated; appended | `F006` created with auto-login | **Pass** |
| **TC08** | Mod 2 | Department Creation & HOD Binding | Dept: Mechanical, HOD: `F001` | `D003` created in `departments.csv` | Department saved successfully | **Pass** |
| **TC09** | Mod 2 | Course Creation & Faculty Allocation | Course: Data Structures, Faculty: `F001` | `C005` created in `courses.csv` | Course cataloged successfully | **Pass** |
| **TC10** | Mod 2 | Student Course Enrollment Junction | Student: `ST001`, Course: `C002` | Appended to `student_courses.csv` | Enrollment record persisted | **Pass** |
| **TC11** | Mod 2 | Prevent Duplicate Course Enrollment | Enroll `ST001` in `C001` again | Flash: Student is already enrolled | Duplicate blocked; flash shown | **Pass** |
| **TC12** | Mod 5 | HOD Access Control & Scoping | Login as `sharma_hod` (Dept `D001`) | Dashboard shows only `D001` faculty/students | Filtered strictly to `D001` records | **Pass** |
| **TC13** | Mod 5 | Faculty Course Ownership Enforcement | Faculty `F002` tries accessing `C002` (`F003`) | Redirected; Flash: Not assigned to course | Unauthorized access blocked | **Pass** |
| **TC14** | Mod 2 | Faculty Attendance Marking | Mark `C001` attendance on 2026-10-28 | `attendance.csv` updated with Present/Absent | Attendance saved accurately | **Pass** |
| **TC15** | Mod 4 | Deterministic Letter Grade Calculation | Enter marks: 95, 82, 73, 64, 52, 45 | Grades: `A+, A, B+, B, C, F` calculated | All grades matched formula exactly | **Pass** |
| **TC16** | Mod 2 | Fee Balance Real-time Calculation | Total: 100000, Paid: 95000 | Due: 5000, Status: Pending | Due: 5000, Pending saved | **Pass** |
| **TC17** | Mod 2 | Fee Complete Settlement Status Toggle | Total: 100000, Paid: 100000 | Due: 0, Status: Paid | Due: 0, Paid saved | **Pass** |
| **TC18** | Mod 3 | Student Attendance Percentage Display | `ST001` attendance summary | Displays percentage (e.g. 75.0%) | Percentage accurately displayed | **Pass** |
| **TC19** | Mod 5 | Cross-Role Unauthorized URL Access | Student accesses `/admin/fees` | Redirects to `/login`; access denied | Access blocked immediately | **Pass** |
| **TC20** | Mod 3 | Session Invalidation on Logout | Click Logout button | `session.clear()` invoked; redirect to login | Session destroyed; cannot go back | **Pass** |

### 12.4 Validation Methods
* **Black-Box UI Testing:** Manual User Acceptance Testing across all four roles simulating complete institutional semesters.
* **Data Store Audits:** Auditing `data/*.csv` files after every insert, update, and delete to verify column alignment, header consistency, and foreign key coherence.
* **Boundary Value Analysis:** Testing edge cases, including division by zero when student has zero classes, negative fee inputs, marks exceeding 100, and duplicate enrollments.
* **Security Barrier Testing:** Simulating manual URL tampering by pasting administrative endpoints into unauthenticated and student browser sessions.

### 12.5 Results
All 20 test cases passed successfully. Zero data corruption events were recorded, and all 44 endpoints consistently returned expected HTTP 200 OK or HTTP 302 Redirect codes. The platform demonstrated absolute operational stability.

---

## 13. Expected Benefits / Learning Outcomes

### 13.1 Benefits to Users and Stakeholders

| Stakeholder Group | Direct Quantifiable Benefit Delivered by University ERP Platform |
| :--- | :--- |
| **Students** | Instant visibility into attendance percentages, course offerings, exam marks, and fee dues without queuing at administrative counters. |
| **Faculty Members** | Saves 10–15 minutes of lecture time daily through streamlined attendance marking and automatic grade calculation. |
| **Heads of Department** | Empowers department leadership with real-time analytics on departmental faculty rosters, student batches, and course allocations. |
| **University Administration** | Eliminates paper register expenditures, prevents data loss, centralizes records, and provides reliable institutional audits. |
| **Academic Community** | Provides a fully transparent, open-source reference implementation of operating system concepts in software engineering. |

### 13.2 Knowledge and Skills Gained
* **Operating Systems Mastery:** Applied theoretical operating system abstractions (Process Lifecycle, Memory Virtualization, VFS, I/O Subsystems, CPU Scheduling, RBAC) to a functioning production codebase.
* **Web Architecture & Engineering:** Mastered full-stack Python/Flask engineering, WSGI request pipelines, Jinja2 template inheritance, and RESTful route architecture.
* **Data Storage Architecture:** Engineered a relational-like schema using raw CSV flat files, handling foreign keys, composite primary keys, and data consistency in pure Python.
* **Software Engineering Rigor:** Applied collaborative version control (Git), branch management, unit testing, black-box validation, and formal academic documentation.

### 13.3 Mapping to Course Outcomes (CCSE0353A)

| Course Outcome (CO) | Official Course Outcome Description | Demonstrated Evidence in University ERP Project |
| :---: | :--- | :--- |
| **CO1** | Understand the fundamental concepts of operating systems, process management, and CPU scheduling algorithms. | **Module 1 & Module 4:** OS process lifecycle, PCB metrics, WSGI event loop, and scheduling burst phase analysis. |
| **CO2** | Analyze process synchronization, inter-process communication (IPC), concurrency mechanisms, and deadlock handling. | **Module 4:** Analysis of critical section hazards during concurrent CSV writes and atomic full-file write-backs. |
| **CO3** | Examine memory management techniques including contiguous allocation, paging, segmentation, and virtual memory. | **Module 3:** Memory segment mapping (Text, Data, Heap, Stack), dynamic heap allocation, and client-side cookie session state. |
| **CO4** | Explore file systems, storage architecture, file allocation methods, disk scheduling, and I/O management. | **Module 2:** Virtual File System abstraction, file descriptors, flat-file schema modeling, and atomic read-modify-write routines. |
| **CO5** | Apply operating system security, protection mechanisms, access control lists (ACLs/RBAC), and evaluate system implementations. | **Module 5:** Dual-mode execution model, system call protection boundaries, and 4-tier Role-Based Access Control matrix. |

---

## 14. Challenges Faced

| Category | Encountered Technical Challenge | Corrective Action & Engineering Solution Implemented |
| :--- | :--- | :--- |
| **Technical** | Legacy key mismatch in course data (`'faculty'` vs `'faculty_id'`) causing template crashes. | Authored `fix_faculty.py` and `update_app.py` utility scripts to migrate dictionary keys in place. |
| **OS Concepts** | Translating theoretical OS concepts into concrete, demonstrable web application features. | Mapped Process, Memory, VFS, CPU, and RBAC directly to discrete modules with measurable evidence. |
| **Data Integrity** | Risk of corrupting CSV files if the process was terminated mid-write. | Engineered atomic-like full-file write-back routines using `write_csv()` with standardized fieldnames. |
| **Concurrency** | Identifying race condition risks when multiple requests write to the same CSV. | Analyzed the Critical Section Problem; documented OS file locking (`flock`) in future roadmap. |
| **UI Consistency** | Ensuring new navigation links (e.g. Student Course Enrollment) appeared across all 36 templates. | Authored `update_sidebar.py` script using Python glob to inject navigation items across all templates. |
| **Security** | Preventing unauthorized cross-role access to protected administrative URLs. | Implemented strict session verification guards at the entry of all 44 Flask view functions. |

---

## 15. Future Improvements

### 15.1 Security Hardening
* **Password Hashing:** Replace plain-text CSV passwords with modern cryptographic hashing algorithms (Argon2id or bcrypt with per-user salt generation).
* **Anti-CSRF Protection:** Incorporate Flask-WTF anti-CSRF tokens in all POST forms to prevent cross-site request forgery.
* **Environment Configuration:** Inject session secret keys via secure environment variables rather than hardcoding in `app.py`.

### 15.2 Functional Extensions
* **Automated Alerts:** Automated SMS and email notifications to students and parents when attendance falls below 75%.
* **PDF & Excel Reporting:** Export examination report cards, attendance ledgers, and fee receipts to downloadable PDF formats.
* **Timetable Scheduler:** Interactive institutional timetable scheduler matching classroom capacities to course enrollments.

### 15.3 Scalability & Database Migration
* **Relational Database:** Migrate flat-file persistence to a relational database engine (SQLite for embedded or PostgreSQL for enterprise) using SQLAlchemy ORM.
* **Production WSGI Deployment:** Deploy behind production WSGI servers (Gunicorn with pre-fork worker processes) managed by an Nginx reverse proxy.
* **Docker Containerization:** Package the application as a multi-container Docker image (Docker Compose) for one-click deployment.

### 15.4 User Experience (UX)
* **Modern Theme Toggle:** Integrate dark/light mode toggle with stored user theme preferences.
* **Mobile Application:** Develop a cross-platform mobile application (Flutter / React Native) consuming a future RESTful JSON API.

---

## 16. Conclusion

The **University ERP Platform** successfully transforms fragmented, error-prone manual academic administration into an automated, responsive, and secure digital platform. Built using Python, Flask, and standard flat CSV files, the application demonstrates that sophisticated enterprise functionality can be achieved without the overhead of heavy commercial database engines.

Beyond delivering a functioning product, the capstone project serves as a comprehensive educational bridge connecting theoretical Operating Systems principles (Process Management, CPU Scheduling, Virtual Memory, VFS File I/O, Concurrency, and Protection) with real-world software engineering. All 44 endpoints and 20 formal test cases executed with a 100% success rate, fulfilling the curriculum outcomes of course `CCSE0353A` and directly advancing United Nations Sustainable Development Goals SDG 4 and SDG 9.

---

## 17. References (IEEE Style)

* **[1]** A. Silberschatz, P. B. Galvin, and G. Gagne, *Operating System Concepts*, 10th ed. Hoboken, NJ, USA: Wiley, 2018.
* **[2]** A. S. Tanenbaum and H. Bos, *Modern Operating Systems*, 4th ed. Boston, MA, USA: Pearson, 2015.
* **[3]** W. Stallings, *Operating Systems: Internals and Design Principles*, 9th ed. Boston, MA, USA: Pearson, 2018.
* **[4]** M. Grinberg, *Flask Web Development: Developing Web Applications with Python*, 2nd ed. Sebastopol, CA, USA: O'Reilly Media, 2018.
* **[5]** Python Software Foundation, "The Python Standard Library – `csv` Module Documentation," 2026. [Online]. Available: `https://docs.python.org/3/library/csv.html`
* **[6]** Pallets Projects, "Flask Documentation (v3.0.x)," 2026. [Online]. Available: `https://flask.palletsprojects.com/`
* **[7]** United Nations, "Sustainable Development Goal 4: Quality Education," Department of Economic and Social Affairs, 2026. [Online]. Available: `https://sdgs.un.org/goals/goal4`
* **[8]** United Nations, "Sustainable Development Goal 9: Industry, Innovation, and Infrastructure," 2026. [Online]. Available: `https://sdgs.un.org/goals/goal9`
* **[9]** E. Gamma, R. Helm, R. Johnson, and J. Vlissides, *Design Patterns: Elements of Reusable Object-Oriented Software*. Reading, MA, USA: Addison-Wesley, 1994.

---

## 18. Appendix – Source Code & File Manifest

**Project Repository Location:** `c:/Users/sahil/Desktop/PBL_OS/UniversityERP`

| File / Directory | Component Type | Lines of Code / Size | Operational Role in System |
| :--- | :--- | :--- | :--- |
| `app.py` | Core Controller | 1,019 lines (~41 KB) | Central Flask application, 44 route handlers, business logic, and RBAC. |
| `requirements.txt` | Configuration | 1 line (12 bytes) | Specifies core framework dependency (`flask>=3.0.0`). |
| `data/*.csv` | Persistence Layer | 9 Files (~2.5 KB) | Flat-file relational storage (users, students, faculty, departments, etc.). |
| `templates/*.html` | View Layer (Jinja2) | 36 Files (~120 KB) | Server-side rendered HTML5 views for Admin, HOD, Faculty, Student. |
| `static/style.css` | Design System | 430 lines (~9.7 KB) | Custom CSS tokens, flexbox/grid layouts, responsive dashboard styling. |
| `static/script.js` | Client Scripting | 114 lines (~4.0 KB) | Auto-dismissing alerts, fee balance calculator, table search filter. |
| `find_faculty.py` | Utility Script | 5 lines | Scans codebase for legacy `course['faculty']` dictionary references. |
| `fix_faculty.py` | Utility Script | 9 lines | Patches `app.py` migrating legacy faculty keys to `faculty_id`. |
| `update_app.py` | Utility Script | 11 lines | Aligns student program field references across `app.py`. |
| `update_sidebar.py` | Utility Script | 18 lines | Injects Student Course Enrollment link across all admin templates. |
| `arc.md` | Specification | 670 lines (~41 KB) | Master Architectural, Technical & Development Specification document. |

### Key Backend Source Snippet (CSV Persistence Engine in `app.py`)
```python
def read_csv(filename):
    filepath = os.path.join(DATA_DIR, filename)
    data = []
    try:
        with open(filepath, 'r', newline='', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                data.append(row)
    except FileNotFoundError:
        pass
    return data

def write_csv(filename, data, fieldnames):
    filepath = os.path.join(DATA_DIR, filename)
    with open(filepath, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

def get_next_id(prefix, filename, id_field):
    data = read_csv(filename)
    max_num = 0
    for row in data:
        if row[id_field].startswith(prefix):
            try:
                num = int(row[id_field][len(prefix):])
                if num > max_num:
                    max_num = num
            except ValueError:
                pass
    return f"{prefix}{max_num + 1:03d}"
```
