# Agent Operating Principles

This document outlines the core principles for the AI agent developing the Agentic System Design Pattern Explorer.

## 1. Architectural Integrity

- **Clarity over cleverness:** The system's design must be explicit and easily understood by senior engineers. Avoid magic or black-box abstractions.
- **Modularity:** Each of the 16 core categories must be implemented as a distinct, composable module.
- **Separation of Concerns:** Maintain a strict separation between the backend (execution engine, pattern library), the frontend (UI/UX), and the documentation.

## 2. Failure-First Design

- **Expose, don't hide:** Every component must be designed to make failures visible, inspectable, and instructive.
- **Assume failure:** Implement fault tolerance not as an afterthought, but as a core design primitive.
- **Test for failure:** Unit and integration tests must explicitly cover failure scenarios, not just the "happy path."

## 3. Executable Mental Models

- **No diagrams without code:** All designs must be represented as executable code.
- **Inspectable state:** The state of any workflow, component, or memory unit must be readily available for inspection at any point in time.
- **Reproducibility:** Every execution run must be replayable and deterministic.

## 4. User-Centric (Elite)

- **Respect the user's expertise:** The UI and API should be designed for power users, not beginners. Avoid oversimplification.
- **Educational depth:** The educational layer is a core feature, not a nice-to-have. It must provide deep, insightful content.

## 5. Development Process

- **Plan-driven:** All significant changes must be preceded by a clear, written plan.
- **Incremental implementation:** Implement the system one category at a time, ensuring each is fully functional before moving to the next.
- **Continuous verification:** After every code modification, verify the change with tests and, where applicable, by running the application.
