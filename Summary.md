# pl/sql
 
## General structure

### DECLARE
Here will be the definitions of all the variables

### BEGIN
The body of the program

### EXCEPTION 
Error handling

### END;

## Types:

### number (Precision, Scale) - 
Numeric values

### varchar2 (1-32767 byte/char)-
String

### boolean – 
True/False

### date

## Two ways to manually define type

### create or replace type strings as table of varchar2(4000);
type object. defined for each schema.

### type strings is table of varchar2(4000);
Local, defined in declare. set for the current block.

## Collections

### 3 types collections:

#### size array-
It has a maximum size

#### Nested table
Its size is dynamic

#### Index-by tables 
1. consist of a set of keys and a set of values that are mapped to them

2. The key must be unique and limited to integer or string types.

3. If we try to change a value in the collection by accessing a key that does not exist, then the key will be added and the value will be mapped under it - this is the way to add members to the collection

## Control flow 

1. if-else
2. case
3. loops

## Exceptions
 Definition: exceptions is a block designed to catch errors in the code and define what happens next.
1. A specific exception can be caught (for example: NO_DATA_FOUND) and "everything else" (any other error not specified) can be caught by OTHERS.
2. We can define exceptions ourselves, in addition to the predefined exceptions

## Cursors
Definition: Cursor is a SQL metadata object. It contains information such as the tabular structure of the results table (in the case of a query), the number of updated records (in the case of a DML command) and more.
1. Contains Cursor Attributes. For example: SQL%ROWCOUNT - will return the number of rows affected by the operation.
2. Cursor can be defined in two ways: by defining a Cursor object (Explicit), or let it be created automatically behind the scenes by using SQL directly (Implicit).

## SQL queries in PL/SQL
1. select into - we will use it to save a return value of a query in variables.
2. If the select query returns no information, we will receive a NO_DATA_FOUND error.
3. You can't just write a query in PL/SQL without the into clause.
4. In places where the into clause can be used, there is an option to add bulk collect and thus get all the results and save them in the collection

## Dynamic SQL

execute immediate - the command provides us with the ability to run dynamic queries.

We would like to run dynamic queries usually in one of the following two cases:
1. When we lack definitional data (schema name, table name, column name, function name, etc.).
2. When we want to run a DDL command.

### into - 
you can add the keyword into, assuming that the result returned from running the query is one line, in order to absorb the result into a variable (whose type matches the type of the result from the query).

### using -
we will use it when we want to add a list (one or more) of parameters to the sql we want to run. We will define the parameters by adding the character ':' in front of them. * Wherever we have to work with dynamic values and we can do it by using parameters, we choose to work with parameters and not with a chain of strings.

### Functions
Defining a function has several parts that are important to explain:

1. or replace - we would like to use it in case we want to override a function with the same name, if it exists.
2. as/is - indicates the beginning of the implementation of the function (in plsql there is really no difference between as and is in functions. However, in SQL there is a difference. 3. For example, in creating a view - one of them will work and the other will not).
4. return - after that we specify the datatype of the value that will be returned from the function.
5. in\out\in out – for out parameters and in parameters, the same principle as in other programming languages.

## Procedures
The principles of a function also exist in a procedure

## Packages
In packages we save functions, procedures as well as types and variables that will be recognized in the scope of the package.

package consists of two parts:

1. declaration - where we will declare the objects we want to expose as an API to the user.
2. body - where we will implement the subprograms we declared as well as additional subprograms for internal use within the package.

## Triggers
Triggers are stored programs that are automatically activated as soon as a certain event happens.

