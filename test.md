# Main Title

## Section Title

### Subsection Title

# SUSE AI on Dell PowerStore

SUSE AI on Dell PowerStore provides an enterprise-ready platform to deploy, manage, monitor, and secure AI workloads using SUSE Rancher Prime, SUSE Observability, SUSE Security, SUSE AI Assistant LIZ, Kubeflow, OpenWebUI, Dell PowerStore, and NVIDIA vGPU-enabled infrastructure.

This hands-on lab offers a guided experience to quickly evaluate SUSE AI running on Dell PowerStore with NVIDIA vGPUs.

Throughout this lab, you will explore how SUSE AI helps simplify AI application deployment, model experimentation, observability, security, and platform operations across a modern cloud-native environment.

---

## Introduction

Before you begin this demo, please take note of the details below to help you proceed through the lab successfully.

This lab demonstrates how SUSE AI can be deployed and operated on Dell PowerStore-backed infrastructure. You will explore the SUSE AI stack, including Rancher Prime, SUSE Observability, SUSE Security, SUSE AI Assistant LIZ, Kubeflow, and OpenWebUI.

By leveraging Dell PowerStore as the storage foundation and NVIDIA vGPUs for accelerated AI workloads, this environment provides a scalable and flexible platform for AI application development, experimentation, management, and monitoring.

This lab is designed to provide a practical understanding of how an enterprise AI platform can be deployed, managed, observed, and secured using SUSE and Dell technologies.

---

# Demo Credentials

While using Edge Browser, please see the links to the webpages below. These webpage links may also be added as bookmarks in the Edge Browser.

Please use the provided credentials exactly as shown.

---

## SUSE AI Cluster / OpenWebUI Information and Credentials

**Web Page:**  
`https://suseai-cluster.demo.local`

**Component:**  
OpenWebUI

**VM Name:**  
`suseai-cluster`

**IP Address:**  
`192.168.1.118`

**VM Login Credentials:**  
Username: `suseai`  
Password: `root123`

**OpenWebUI Login Credentials:**  
Username: `suseai`  
Password: `root123`  
Email: `suseai@suse.com`

---

## SUSE AI Assistant LIZ Information and Credentials

**Web Page:**  
`https://liz.suseai.demo.local`

**Component:**  
LIZ AI Assistant

**VM Name:**  
`suseai-cluster`

**IP Address:**  
`192.168.1.118`

**VM Login Credentials:**  
Username: `suseai`  
Password: `root123`

**LIZ AI Assistant Login Credentials:**  
Username: `admin`  
Password: `@SD123fgh456`

---

## Kubeflow Information and Credentials

**Web Page:**  
`http://kubeflow-suseai.demo.local`

**Component:**  
Kubeflow

**VM Name:**  
`suseai-kubeflow`

**IP Address:**  
`192.168.1.130`

**VM Login Credentials:**  
Username: `suseai`  
Password: `root123`

**Kubeflow Login Credentials:**  
Email: `user@example.com`  
Password: `12341234`

---

## SUSE Rancher Prime Information and Credentials

**Web Page:**  
`http://rancher-prime.demo.local`

**Component:**  
Rancher Prime

**VM Name:**  
`SUSEAI-Rancher Prime`

**IP Address:**  
`192.168.1.103`

**VM Login Credentials:**  
Username: `suseai-user`  
Password: `root123`

**Rancher Prime Login Credentials:**  
Username: `admin`  
Password: `@SD123fgh456`

---

## SUSE Observability Information and Credentials

**Web Page:**  
`http://suse-observability.demo.local`

**Component:**  
SUSE Observability

**VM Name:**  
`observability-f`

**IP Address:**  
`192.168.1.129`

**VM Login Credentials:**  
Username: `suseai`  
Password: `root123`

**SUSE Observability Login Credentials:**  
Username: `admin`  
Password: `@SD123fgh456`

---

## SUSE Security Information and Credentials

**Web Page:**  
`http://rancher-prime.demo.local`

**Component:**  
SUSE Security

**Access Method:**  
Use the NeuVector extension from Rancher Prime to access SUSE Security.

**VM Name:**  
`security`

**IP Address:**  
`192.168.1.117`

**VM Login Credentials:**  
Username: `suseai`  
Password: `root123`

**SUSE Security Login:**  
Access through the NeuVector extension in Rancher Prime.

---

# Environment Summary

| Component | Web Page | VM Name | IP Address | Login |
|---|---|---|---|---|
| OpenWebUI | `https://suseai-cluster.demo.local` | `suseai-cluster` | `192.168.1.118` | `suseai / root123` |
| LIZ AI Assistant | `https://liz.suseai.demo.local` | `suseai-cluster` | `192.168.1.118` | `admin / @SD123fgh456` |
| Kubeflow | `http://kubeflow-suseai.demo.local` | `suseai-kubeflow` | `192.168.1.130` | `user@example.com / 12341234` |
| Rancher Prime | `http://rancher-prime.demo.local` | `SUSEAI-Rancher Prime` | `192.168.1.103` | `admin / @SD123fgh456` |
| SUSE Observability | `http://suse-observability.demo.local` | `observability-f` | `192.168.1.129` | `admin / @SD123fgh456` |
| SUSE Security | `http://rancher-prime.demo.local` | `security` | `192.168.1.117` | Access through NeuVector extension |

---

# Welcome to the SUSE AI on Dell PowerStore Hands-on Lab

Welcome to the **SUSE AI on Dell PowerStore** hands-on lab.

This hands-on demonstration provides a comprehensive understanding of how SUSE AI can be used to deploy, operate, monitor, and secure AI workloads on Dell PowerStore-backed infrastructure with NVIDIA vGPU acceleration.

We suggest following the lessons in order. However, you are free to navigate and review the environment as needed.

Throughout this lab, you will explore the SUSE AI platform, its capabilities, and the user interfaces used to manage AI workloads. You will also learn how Rancher Prime provides centralized Kubernetes management, how Kubeflow supports machine learning workflows, how OpenWebUI enables interaction with AI models, how SUSE Observability provides visibility into platform health, and how SUSE Security helps protect cloud-native workloads.

---

## Duration

This lab is designed to be completed in approximately **45 minutes** in one sitting, but you can come back and pick up where you left off.

---

## Objective

The objective of this lab is to familiarize you with the capabilities of SUSE AI on Dell PowerStore, allowing you to:

1. Explore the essential features of SUSE AI.
2. Access and validate SUSE AI application interfaces.
3. Understand how Rancher Prime provides centralized Kubernetes management.
4. Use OpenWebUI to interact with AI services.
5. Explore SUSE AI Assistant LIZ for AI-assisted operations.
6. Access Kubeflow for AI and machine learning workflow management.
7. Monitor infrastructure and application health using SUSE Observability.
8. Explore SUSE Security using the NeuVector extension in Rancher Prime.
9. Understand how Dell PowerStore supports AI workloads with scalable, reliable, high-performance storage.
10. Review how NVIDIA vGPUs enable accelerated AI workload execution.

---

## Hands-on Experience

During this lab, you will gain practical experience and will be able to do the following:

1. Navigate the SUSE Rancher Prime interface.
2. Review the SUSE AI cluster and related workloads.
3. Access OpenWebUI and validate AI model interaction.
4. Access SUSE AI Assistant LIZ and explore assistant-driven capabilities.
5. Access Kubeflow and review machine learning workflow functionality.
6. Use SUSE Observability to assess platform health, metrics, service status, and topology.
7. Access SUSE Security through the NeuVector extension in Rancher Prime.
8. Review the role of Dell PowerStore in supporting persistent storage for AI workloads.
9. Understand the relationship between SUSE AI services, Kubernetes, storage, observability, and security.
10. Explore the environment at your own pace after completing the guided sections.

---

## Lesson Completion

The completion time for each lesson may vary depending on your chosen tasks and level of exploration.

It is important to note that this lab operates in a demo environment. Some functionality may not fully replicate a real-world production deployment.

---

# Lab Rules

Please follow the lab rules below to avoid impacting the shared demo environment:

1. Please **DO NOT** change any IP addresses.
2. Please **DO NOT** shut down any virtual machines.
3. Please **DO NOT** restart any virtual machines unless instructed.
4. Please **DO NOT** modify network interfaces.
5. Please **DO NOT** delete any Kubernetes clusters.
6. Please **DO NOT** delete any Kubernetes nodes.
7. Please **DO NOT** delete namespaces, workloads, services, ingress objects, storage classes, persistent volumes, or persistent volume claims.
8. Please **DO NOT** delete any Dell PowerStore resources that you have not created.
9. Please **DO NOT** run performance or stress tests.
10. Please **DO NOT** change admin passwords.
11. Please **DO NOT** remove Rancher Prime integrations, extensions, or cluster connections.
12. Please **DO NOT** disable SUSE Observability components.
13. Please **DO NOT** disable SUSE Security or NeuVector components.
14. Please **DO NOT** modify enforcement policies unless specifically instructed.
15. Please only create, edit, or delete resources when instructed by the lab guide.

---

# This Hands-on Lab Contains the Following Modules

1. Required Pre-step: Validate Lab Access
2. Module 1: Accessing Rancher Prime
3. Module 2: Reviewing the SUSE AI Kubernetes Cluster
4. Module 3: Accessing OpenWebUI
5. Module 4: Accessing SUSE AI Assistant LIZ
6. Module 5: Accessing Kubeflow
7. Module 6: Accessing SUSE Observability
8. Module 7: Accessing SUSE Security through Rancher Prime
9. Module 8: Reviewing SUSE AI Infrastructure Virtual Machines
10. Module 9: Exploring Dell PowerStore Integration
11. Module 10: Reviewing NVIDIA vGPU-enabled AI Workloads
12. Final Review

---

# REQUIRED: Pre-step - Validate Lab Access

Before beginning the lab, validate that the main interfaces are available from the Edge Browser.

## Steps

1. Open the Edge Browser.
2. Confirm that the following URLs are accessible:

   - `http://rancher-prime.demo.local`
   - `https://suseai-cluster.demo.local`
   - `https://liz.suseai.demo.local`
   - `http://kubeflow-suseai.demo.local`
   - `http://suse-observability.demo.local`

3. If a certificate warning appears, proceed to the site.
4. Confirm that each page loads successfully.
5. Do not log in to all pages yet. Login steps are covered in each module.

## Expected Result

You should be able to access the landing or login page for each SUSE AI component.

If a page does not load immediately, wait a few minutes and refresh the page.

---

# Module 1: Accessing Rancher Prime

In this module, you will access Rancher Prime and review the SUSE AI Kubernetes environment.

Rancher Prime enables centralized control of Kubernetes clusters, simplifying operations, governance, and workload management. In this lab, Rancher Prime is used as the primary management interface for the SUSE AI environment.

## Steps

1. Open the Edge Browser.
2. Navigate to Rancher Prime:

   `http://rancher-prime.demo.local`

3. Log in using the following credentials:

   Username: `admin`  
   Password: `@SD123fgh456`

4. After login, review the Rancher Prime dashboard.
5. Locate the available Kubernetes cluster associated with the SUSE AI environment.
6. Click the cluster to review its status.
7. Review the cluster dashboard.
8. Observe the following areas:

   - Cluster health
   - Nodes
   - Workloads
   - Namespaces
   - Storage resources
   - Apps
   - Extensions
   - Monitoring or security-related integrations

9. Confirm that the cluster is available and healthy.

## Expected Result

You should be successfully logged in to Rancher Prime and able to view the SUSE AI Kubernetes cluster.

## Notes

Please feel free to explore the Rancher Prime interface, but do not modify or delete any existing resources.

---

# Module 2: Reviewing the SUSE AI Kubernetes Cluster

In this module, you will review the Kubernetes cluster used by the SUSE AI environment.

The SUSE AI platform runs on Kubernetes and uses multiple services to provide AI, observability, security, and management capabilities.

## Steps

1. From Rancher Prime, open the SUSE AI Kubernetes cluster.
2. Navigate to the cluster dashboard.
3. Review the overall cluster state.
4. Navigate to **Nodes**.
5. Review the available nodes and their health.
6. Navigate to **Workloads**.
7. Review the running workloads related to SUSE AI services.
8. Navigate to **Namespaces**.
9. Look for namespaces related to:

   - AI services
   - Kubeflow
   - Observability
   - Security
   - System components

10. Navigate to **Storage** if available.
11. Review storage classes, persistent volumes, and persistent volume claims.

## Expected Result

You should be able to view the SUSE AI cluster resources and confirm that the environment is running.

## Notes

Do not delete workloads, namespaces, storage objects, or cluster-level resources.

---

# Module 3: Accessing OpenWebUI

In this module, you will access OpenWebUI and validate the AI user interface.

OpenWebUI provides a simple interface for interacting with AI models and services. It allows users to send prompts, review responses, and validate that the AI application layer is functioning correctly.

## Steps

1. Open a new browser tab.
2. Navigate to OpenWebUI:

   `https://suseai-cluster.demo.local`

3. Log in using the following credentials:

   Username: `suseai`  
   Password: `root123`  
   Email: `suseai@suse.com`

4. After login, review the OpenWebUI interface.
5. Start a new chat session.
6. Enter the following sample prompt:

   ```text
   Explain what SUSE AI on Dell PowerStore is in simple terms.
