# Task 9: Claude Code Skills for Book Generation

## Overview

This directory contains 5 custom Claude Code Skills designed to automate and enhance the book writing process, created for the 30-Day AIDD Challenge Task 9.

## Skills Included

### 1. 📖 Chapter Outline Generator

**Location**: `.claude/skills/chapter-outline-generator/SKILL.md`

Creates comprehensive chapter outlines with:

- Chapter titles and summaries
- Learning objectives
- Hierarchical sections and subsections
- Word count estimates
- Logical flow validation

**Best for**: Planning new books, restructuring existing content, creating tables of contents

---

### 2. 🎭 Character Development Assistant

**Location**: `.claude/skills/character-development-assistant/SKILL.md`

Develops deep, multi-dimensional characters with:

- Physical appearance and mannerisms
- Personality framework (strengths, flaws, quirks)
- Detailed backstory and formative events
- Motivations, fears, and desires
- Relationship mapping
- Character arc development

**Best for**: Fiction writing, developing compelling protagonists and antagonists

---

### 3. 🔍 Plot Consistency Checker

**Location**: `.claude/skills/plot-consistency-checker/SKILL.md`

Analyzes narrative for:

- Timeline inconsistencies
- Character continuity errors
- Plot holes and unresolved threads
- World-building contradictions
- POV violations
- Pacing issues

**Best for**: Revision stage, catching errors before publication

---

### 4. 🔬 Research and Fact-Checking Tool

**Location**: `.claude/skills/research-fact-checker/SKILL.md`

Assists with:

- Research strategy development
- Fact verification (historical, scientific, cultural)
- Anachronism detection
- Source bibliography management
- Techniques for integrating research naturally

**Best for**: Historical fiction, non-fiction, sci-fi requiring accuracy

---

### 5. ✨ Grammar and Style Enhancer

**Location**: `.claude/skills/grammar-style-enhancer/SKILL.md`

Provides:

- Grammar and mechanics checking
- Style improvement (passive→active, weak→strong verbs)
- Clarity and concision recommendations
- Consistency checking (tense, POV, spelling)
- Readability metrics

**Best for**: Final polishing, maintaining author voice while fixing errors

---

## Directory Structure

```
Task_09/
├── .claude/
│   ├── commands/                    # SpecKit commands
│   └── skills/                      # Custom Skills
│       ├── chapter-outline-generator/
│       │   └── SKILL.md
│       ├── character-development-assistant/
│       │   └── SKILL.md
│       ├── plot-consistency-checker/
│       │   └── SKILL.md
│       ├── research-fact-checker/
│       │   └── SKILL.md
│       └── grammar-style-enhancer/
│           └── SKILL.md
├── README.md                        # This file
└── SUBMISSION.md                    # Official submission document
```

---

## How to Use These Skills

### Activating Skills in Claude Code

Claude Code will automatically detect and use these skills when:

1. The `.claude/skills/` directory is present in your project
2. Each skill has a properly formatted `SKILL.md` file with YAML frontmatter
3. You describe a task that matches the skill's description

### Example Usage

**For Chapter Outline Generator**:

> "I need help outlining a mystery novel with 12 chapters"

**For Character Development Assistant**:

> "Create a detailed character profile for my protagonist, a detective in 1920s New York"

**For Plot Consistency Checker**:

> "Check my first 5 chapters for timeline inconsistencies and plot holes"

**For Research Tool**:

> "I'm writing historical fiction set in Victorian London. What should I research?"

**For Grammar Enhancer**:

> "Polish this chapter for grammar and style while keeping my voice"

---

## Skill Format

Each skill follows the official Claude Code Skills structure:

### YAML Frontmatter

```yaml
---
name: skill-name
description: Brief description (max 1024 chars)
---
```

### Content Sections

1. **Purpose**: What the skill does
2. **When to Use**: Activation triggers
3. **Instructions**: Step-by-step process
4. **Examples**: Concrete demonstrations
5. **Tips**: Best practices
6. **Validation**: Quality checklist

---

## Why These Skills?

### Complete Book Workflow Coverage

- **Planning**: Chapter Outline Generator
- **Development**: Character Development Assistant
- **Writing**: Research and Fact-Checking Tool
- **Revision**: Plot Consistency Checker, Grammar and Style Enhancer

### Real Value Addition

- ✅ Automate repetitive tasks
- ✅ Maintain quality and consistency
- ✅ Save time on research and fact-checking
- ✅ Catch errors early
- ✅ Preserve author's unique voice

### Reusability

All skills are designed for use across multiple book projects, not just one-time use.

---

## Technical Details

### Compatibility

- Claude Code Desktop
- Claude AI with MCP (Model Context Protocol)
- Follows official Claude Skills specification

### File Structure Requirements

- Skills must be in `.claude/skills/` directory
- Each skill in its own subdirectory
- Main file must be named `SKILL.md`
- YAML frontmatter required

### Testing

Each skill includes:

- Multiple examples (fiction and non-fiction)
- Validation checklists
- Clear output formats
- Voice preservation guidelines

---

## Submission Information

**Task**: Task 9 — Custom Claude Code Skills  
**Instructor**: Sir Hamzah Syed  
**Deadline**: 3 Days from assignment  
**Slot**: Friday — 6:00 PM to 9:00 PM

**Submission Includes**:

1. ✅ 5 custom skills for book generation
2. ✅ `.claude/skills/` directory structure
3. ✅ Comprehensive documentation (`SUBMISSION.md`)
4. ✅ Screenshot of VSCode Explorer

---

## Learning Outcomes

By creating these skills, I've learned:

1. **Claude Code Skills Architecture**: How to structure reusable AI capabilities
2. **YAML Frontmatter**: Proper skill metadata format
3. **Instruction Design**: Writing clear, actionable prompts for AI agents
4. **Domain Expertise**: Deep understanding of book writing workflow
5. **Sub-Agent Concepts**: How specialized agents work together in a system

This knowledge directly applies to the upcoming **Hackathon** and future agentic AI development.

---

## Future Enhancements

Potential additions:

- **Dialogue Polisher**: Enhance character conversations
- **Scene Builder**: Construct compelling scenes with proper structure
- **World-Building Assistant**: Develop consistent fictional worlds
- **Publishing Formatter**: Format manuscripts for different publishers
- **Beta Reader Simulator**: Provide reader feedback perspective

---

## Contact

**Created by**: Abdul Samad Siddiqui  
**Date**: December 10, 2024  
**Challenge**: 30-Day AIDD Challenge  
**Repository**: 30-Day-AIDD-Challenge-Task-1

---

## License

These skills are created for educational purposes as part of the Governor House AI course curriculum.
