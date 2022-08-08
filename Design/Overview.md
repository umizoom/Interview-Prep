## SOLID Definition

- Single-responsiblity Principle
- Open-closed Principle
- Liskov Substitution Principle
- Interface Segregation Principle
- Dependency Inversion Principle


### Single-responsiblity Principle

A class should do one thing, therefore it should have only a single reason to change.

Following the Single Responsibility Principle is important. First of all, because many different teams can work on the same project and edit the same class for different reasons, this could lead to incompatible modules.

Second, it makes version control easier. For example, say we have a persistence class that handles database operations, and we see a change in that file in the GitHub commits. By following the SRP, we will know that it is related to storage or database-related stuff.


### Open-Closed Principle

Classes should be open for extension and closed to modification.

### Liskov Substitution Principle 

States that subclasses should be substitutable for their base classes.

This means that, given that `class B` is a subclass of `class A`, we should be able to pass an object of `class B` to any method that expects an object of `class A` and the method should not give any weird output in that case.

### Interface Segregation Principle

The principle states that many client-specific interfaces are better than one general-purpose interface. Clients should not be forced to implement a function they do no need.