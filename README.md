# AI Decision Automation

A simple Python automation project where an AI-style decision decides what is important,
then the automation keeps only those items.

## What it does

- Takes a list of messages
- Decides which ones are important (decision step)
- Outputs only important messages

## Why this matters

Shows the core AI automation pattern:
input → decision → action → output

## n8n Workflow

The n8n workflow (`n8n/decision_workflow.json`) implements the automation flow:
Manual Trigger → HTTP Request to backend → IF/ELSE routing → actions.
Import the JSON into n8n to load the workflow.

## Run locally

```bash
pip install -r requirements.txt
uvicorn app:app --reload
```
