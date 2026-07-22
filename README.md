# Polymorphism - Smart Traffic Management System

## Project Overview
This repository contains a Python implementation demonstrating the concept of **Polymorphism** in Object-Oriented Programming (OOP) within a Smart City traffic control context.

## Problem Description
In a smart city, various intelligent devices perform distinct operational tasks upon receiving a uniform command (`activate()`). Polymorphism allows us to iterate through a collection of different device objects and invoke their common interface method without needing to check or care about their specific class type.

## Class Architecture
* **Parent Class:** `TrafficDevice`
* **Child Classes:**
  * `TrafficLight`
  * `SpeedCamera`
  * `PedestrianSignal`
  * `EmergencySiren`

## Key Concept Demonstrated
- **Polymorphism & Extensibility:** Adding a new class like `EmergencySiren` requires zero modification to the core execution loop. The loop iterates through the list of devices and dynamically calls the appropriate `activate()` implementation for each object.

## How to Run
```bash
python main.py
