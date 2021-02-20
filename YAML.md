## What is YAML?

- Data-orientated human readable serialization language
- Yet Another Markup Language
- most commonly referred to as 'YAML Ain't Markup Language'

## YAML elements

- mostly based on Key-Value pairs ```Name: Value```
- or a key with a complex/compound value:
  - 
  ```
  Name: < the key<br />
     AnotherName: someValue < the value
  ```
- YAML is a superset of JSON
  - can utilize JSON style sequences and maps
  -
  ```
  a_json_style_map: {"K": "V"}<br />
  a_json_style_sequence: ["pink", "red", "red", "cat", 123, 234, 345]
  ```

- Spaces/indenting
  - should indent with space
  - Must be spaces between element part
  - ```Key: Value``` is correct
  - ```Key:Value``` is not correct (no space after the colon)

- Begin/End document
  - defining the start and end of the document is optional
  - start : '---' 
  - end : '...'
  
## 출처
- [5분](https://www.codeproject.com/Articles/1214409/Learn-YAML-in-five-minutes)
- [Github action workflow](https://docs.github.com/en/actions/reference/workflow-syntax-for-github-actions)
