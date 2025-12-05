# Password Strength Utility Library

## Overview
This project provides a comprehensive password-strength utility library designed to evaluate, analyze, and improve password security.  
The library includes 15+ fully documented Python functions that validate password components, calculate entropy, detect repeated patterns, generate strong passwords, and provide complete strength assessments.

These functions will later be refactored into object-oriented classes for Project 02.

---

## Team Member
- **Abdullah Khan** – Developer & Documentation Author

---

## Problem Statement
Weak passwords are one of the most common cybersecurity vulnerabilities. Many users create short, predictable, or commonly used passwords that attackers can easily guess through brute force, dictionary attacks, or pattern recognition.

This project addresses that problem by developing a modular password utility library that can:
- Validate password structure  
- Check for uppercase, lowercase, digits, and special characters  
- Calculate estimated password entropy  
- Detect repeated or predictable patterns  
- Identify common or weak passwords  
- Generate strong random passwords  
- Provide detailed evaluation summaries  

The goal is to create a reusable and maintainable codebase that supports secure authentication systems.

---

## Repository Structure

C:.
│   .gitignore
│   LICENSE
│   README.md
│
├───docs
│       function_reference.md
│       usage_examples.md
│
├───examples
│       demo_script.py
│
└───src
    │   library_name.py
    │   __init__.py