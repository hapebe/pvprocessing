#!/bin/bash
curl -X POST http://localhost:8000/todo \
     -H "Content-Type: application/json" \
     -d '{"name": "HaPes Todo Item", "description": "This is a description", "done": false}'
curl -X POST http://localhost:8000/todo -H "Content-Type: application/json" -d '@item1.json'
curl -X POST http://localhost:8000/todo -H "Content-Type: application/json" -d '@item2.json'