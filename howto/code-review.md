# 1 Million Women To Tech (1MWTT) Code Review #HOWTO

This document is to help you Give and Receive code reviews. Mentors are the ones giving the code reviews, while Students receive them.

It is important for reviewers to be kind, and for receivers to be, well, receptive to suggestions.



# Format

### Praise

Always start with positive feedback. e.g. Great job. You have come this far. Well done. Add something that you noticed the student did really well.

### Grading rubric

Generic Rubric | Needs improvement | Good | Outstanding 
 :--- | :---: | :---: | :---: 
**Effort** |||
**Solution** |||
`Code formatting`|||
`Architecture`|||
`Coding best practices`|||
`Non Functional requirements`|||
`OOAD or SOLID principles (if applicable)`|||

### Comments
- BRAVOs
- Suggestions
- Grade
- Level

### Ideas for optional discussion points for the BRAVOs and suggestions

#### Code formatting
While going through the code, check the code formatting to improve readability and ensure that there are no blockers:
- Enforce language style guide automatically: prettify, lint.
- Use alignments (left margin), proper white space. Also ensure that code block starting point and ending point are easily identifiable.
- Ensure that proper naming and coding conventions (Pascal, camelCase etc.) have been followed. 
- Code should fit in the standard 14 inch laptop screen.  There shouldn’t be a need to scroll horizontally to view the code. In a 21 inch monitor, other windows (toolbox, properties etc.) can be opened while modifying code, so always write code keeping in view a 14 inch monitor.
- Remove the commented code as this is always a blocker, while going through the code. Commented code can be obtained from Source Control (like Git), if required.

#### Architecture
- The code should follow the defined architecture.
- Separation of Concerns followed
- Split into multiple layers and tiers as per requirements (Presentation, Business and Data layers).
- Split into respective files (HTML, JavaScript and CSS).
- Code is in sync with existing code patterns/technologies.
- Design patterns: Use appropriate design pattern (if it helps), after completely understanding the problem and context.

#### Coding best practices

- No hard coding, use constants/configuration values.
- Group similar values under an enumeration (enum).
- Comments – Do not write comments for what you are doing, instead write comments on why you are doing. Specify about any hacks, workaround and temporary fixes. Additionally, mention pending tasks in your to-do comments, which can be tracked easily.
- Avoid multiple if/else blocks.
- Use framework features, wherever possible instead of writing custom code.
- **Use early exits**
- **Return booleans if possible**

#### Non Functional Requirements

- Maintainability
  - Readability
  - Testability
  - Debuggability
  - Configurability
- Reusability
  - **DRY**
  - Components
  - Generic
  - Write "shy" code
- Reliability
  - Exception handling
  - Cleanup
Extensibility
Security
Performance
Scalability
Usability
OOAD
- SRS
- Open Closed Principle
- Liskov
- Interface segregation
- Dependency injection

### End with praise

Like in the openining you want to give encouragment and appreciation. e.g. You have come so far, well done! Great work! BRAVO. Impressive. Great sense of humour! ;)


(# previous feedback)

https://github.com/CristyTarantino/toolkitten/projects/1
https://github.com/CristyTarantino/toolkitten/pull/3

# Resources

checklist
- https://www.evoketechnologies.com/blog/code-review-checklist-perform-effective-code-reviews/

tips
- https://www.evoketechnologies.com/blog/simple-effective-code-review-tips/

specific examples e.g. DRY
- https://medium.com/@same7mabrouk/the-checklist-of-my-code-review-18cc6f6fb5b3
(fun picture, includes the GitHub illustration of PR flow: 
- https://guides.github.com/introduction/flow/)

good examples
- https://medium.com/@andreigridnev/examples-of-code-review-checklists-and-guides-2dfed082a86d

fun cartoons
- xkcd: Code Quality https://xkcd.com/1513/
- xkcd: Code Quality 2 https://xkcd.com/1695/
- xkcd: Code Quality 3 https://m.xkcd.com/1833/

best practices
- https://medium.com/palantir/code-review-best-practices-19e02780015f 
- https://smartbear.com/learn/code-review/best-practices-for-peer-code-review/
- https://smartbear.com/resources/ebooks/the-state-of-code-review-2018/
- https://www.ibm.com/developerworks/rational/library/11-proven-practices-for-peer-review/index.html
- https://gist.github.com/kashifrazzaqui/44b868a59e99c2da7b14

report
- https://smartbear.com/SmartBear/media/ebooks/The-2018-State-Of-Code-Review-by-SmartBear.pdf

# Why code review?

1. Better than grades

2. Real life

3. Best way to learn
