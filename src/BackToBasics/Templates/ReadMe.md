# Templates

In the **1970's**, some languages began allowing algorithms to be written in terms of types to-be-specified-later.

## Different Types of Templates

In C++ we have **six** different types of templates:
1. Function Templates (C++98/03)
2. Class Templates (C++98/03)
3. Member Function Templates (C++98/03)
4. Alias Templates (C++11)
5. Variable Templates (C++14)
6. Lambda Templates (C++20)

### Function Templates
```c++
template<class T>
T const& min(T const& a, T const& b) {
    return (a < b) ? a : b;
}

template<class T>
void swap(T& a, T& b);

template<class RandomIt, class Compare>
void sort(RandomIt first, RandomIt last, Compare comp);
```
### Class Templates
```c++
template<class T, size_t N>
struct array{...};

template<class T, class Alloc = allocator<T>>
class vector{...};

template<class Key, class Val, class Compare = less<Key>, class Allocator = allocator<pair<const Key, T>>>
class map{...};
```
### Member Function Templates
```c++
template<class T, class Alloc = allocator<T>>
class vector
{
public:
...
using iterator = ...;
using const_iterator = ...;
...
template<class InputIter>
iterator insert(const_iterator pos, InputIter first, InputIter last) {...}
...
};

// or for out of class definition

template<class T, class Alloc = allocator<T>>
using iterator = vector<T, Alloc>::iterator;
using const_iterator = vector<T, Alloc>::const_iterator;

template<class T, class Alloc = allocator<T>>
template<class InputIter>
iterator vector<T, Alloc>::insert(const_iterator pos, InputIter first, InputIter last){...}
```
### Alias Templates (C++11)

Here we use the template and then the using keywords.

```c++
template<class T>
using sa_vector = vector<T, my_special_allocator<T>>;
sa_vector<float> fv;

template<class Key, class Val>
using my_map = map<Key, Val, greater<Key>>;
my_map<string, int> msi;

template<class T, ptrdiff_t C, class A = std::allocator<T>, class CT = void>
using general_row_vector =
basic_matrix<matrix_storage_engine<T, extents<1,C>, A, matrix_layout::row_major>, CT>;
general_row_vector<double, 20> rv;
```
### Variable Templates (C++14)
```c++
template<class T>
inline constexpr T pi = T(3.1415926535897932385L);

template<class T>
T circular_area(T r) { return pi<T> * r * r; }

// is_arithmetic is a concept.
template<class T>
inline constexpr bool is_arithmetic_v = is_arithmetic<T>::value;

void init(T* p, size_t N)
{
    // compile time if expression. Meaning at run time there won't be a loop.
    if constexpr (is_arithmetic<T>)
        memcpy(p, 0, sizeof(T) * N);
    else
        uninitialized_fill_n(p, N, T());
}
```

### Lambda Templates (C++20)
```c++
auto multiply = []<class T>(T a, T b) { return a * b; };
auto d0 = multiply(1.0, 2.0);
```

## Template Terminology
How do we refer to templates used to "generate" classes?
- Classes, structs, and unions are referred to generally as *class types*
- *Class template* indicates a parametrized description of a family of classes

C++ also provides parametrized descriptions of
- Functions
- Member functions
- Type aliases
- Variables
- Lambdas

The standard treats terms thing template consistently
- template is the noun, indicating a parametrized description
- thing is an adjective, specifying the family of things being parametrized
So we have, class template, function template. Note that the asscociated verb is *parameterize*.

## Compiling and Linking

### Compilation

The process of converting human readable source code into binary object files.
From a high-level perspective, there are four stages of compilation:
- Lexical Analysis
- Syntax Analysis
- Semantic Analysis
- Code Generation

In C++, we typically generate one object file for each source file. The standard calls the compilation process **translation**.

### Linking

The Process of combining object files and binary libraries to make a working program.

## Translation Units

In C++ compiling happens in **nine** well-defined steps. Phases 1 to 6 do **lexical** analysis, this we call **preprocessing**. Output of stage 6 is called a **translational unit** in the standard.

Phases **7 and 8** perform syntax analysis, semantic analysis, codegen.
These are what we usually refer to as compilation.
Templates are *parsed* in Phase 7.
Templates are *instantiated* in Phase 8.
The output os called a translated translation unit. (e.g. object code)

Phase 9 performs program image create.
This is what we usually think of as *linking*.
The output is an executable image suitable for the intended execution environment.

## Declaration vs Definition

An entity is one of these things in C++:
- value
- object
- reference
- structured binding
- function
- enumerator
- type
- class member
- bit-field
- template
- template specialization
- namespace
- pack

An entity gets a name. A name is the use of an identifier that denotes an entity (or label). Every name that denotes an entity is introduced by a *declaration*. 

A **declaration** introduces one or more *names* into the *translation unit*. Note that, a declaration can and may *re-introduce* a name into a translation unit.

A **definition** is a declaration that fully defines the entity being introduced.

A **variable** is an entity introduced by the declaration of an object or of a reference other than a non-static data member. In other words,
in C++ non-static data member (Class Field) is not referred as a *variable*.

Every declaration is also a definition, unless:

- It is a function declaration without a corresponding definition of the body
    ```c++
    int doSomething(int);
    ```
- It is a parameter declaration in a function declaration that is not a definition
  ```c++
  int doSomething(int const& param)
  ```
- It is a declaration of a class name without a corresponding definition
    ```c++
    class vector;
    ```
- It is a template parameter
    ```c++
    // T and N are type entities introduced by template declaration.
    template<class T, size_t N>
    class vector;
    ```
- It is a typedef declaration
- It is a using declaration
  ```c++
  // Introduces UInt name intro translation unit.
  using UInt = size_t; 
  ```
- It contains the extern specifier
  ```c++
  // Explicitly, marks a name and sets its linking to external linking.
  extern int doSomething(int param);
  ```
- And a few other cases...

The set of definitions is a proper subset of the set of declarations. Look at the slides pages 36 and 37.
  
## Some notes on extern keyword

The **extern** keyword, marks the linkage of an entity to be external. That means we tell the compiler to not worry about the definition of the entity if it is not in the current translation unit, since the definition will be in other translation units and that will be resolved at linking stage.
```c++
// non-const global variable.
// specifies that the variable or function is defined in another translation unit.
// The extern must be applied in all files except the one where the variable is defined.
extern int i;

// const global variable.
// specifies that the variable has external linkage. 
// The extern must be applied to all declarations in all files.
extern const int i;
```
## One Definition Rule (ODR)

A given translation unit can contain at most one definition of any:
- variable
- function
- class type
- enumeration type
- template
- default argument for a parameter for a function in a given scope;
  [Read this regarding default arguments](https://en.cppreference.com/w/cpp/language/default_arguments).
- default template argument

There may be multiple declarations, but there can only be one definition.

A program must contain exactly one definition of every non-inline variable
or function that is used in the program

- Multiple declarations are OK, but only one definition
- For an inline variable or an inline function, a definition is required in every
translation unit that uses it
- inline was originally a suggested optimization made to the compiler
- It has now evolved to mean **"multiple definitions are permitted"**
- Exactly one definition of a class must appear in any translation unit that uses
it in such a way that the class must be complete
- The same rules for inline variables and functions also apply to templates

Advices on observing ODR:
- For an **inline entity** (variable or function) that get used in a translation unit, make sure it is defined at least once somewhere in that translation unit
- For a **non-inline, non-template** entity that gets used, make sure it is
defined exactly once in across all translation units
- For a **template entity**, define it in a header file, include the header where
the thing is needed, and let the toolchain decide where it is defined
- Except in rare circumstances where finer control is required

## Template Parameters and Template Arguments

- **Template parameters** are the names that come after the *template keyword*
in a *template declaration*. 
- **Template arguments** are the concrete items substituted for template
parameters to create a template **specialization**.

```c++
// T1 and T2 are Template Parameters
template<class T1, class T2>
struct pair
{
    T1 first;
    T2 second;
    ...
};
// T is a Template Parameter
template<class T>
T const& max(T const& a, T const& b)
{ ... }
---
// string, double, and double, are Template Arguments
pair<string, double> my_pair;

double d = max<double>(0, 1);

string s1 = ...;
string s2 = ...;
string s3 = max(s1, s2);

```

### Template Parameters

Template parameters come in three flavors
- Type parameters
- Non-type template parameters (NTTPs)
- Template-template parameters

**Type parameters**
- **Most common**
- Declared using the **class** or **typename** keywords
```c++
template<class T1, class T2> struct pair;

template<typename T1, typename T2> struct pair;

template<class T> T max(T const& a, T const& b);

template<typename T> T max(T const& a, T const& b);
```

**Non-Type Template Parameters (NTTPs)**
Template parameters don't have to be types:
```c++
template<class T, size_t N>
class Array
{
    T m_data[N]
    ...
};
Array<foobar, 10> some_foobars;

---

template<int Incr>
int IncrementBy(int val)
{
    return val + Incr;
}
int x = ...;
int y = IncrementBy<42>(x);
```
NTTPs denote constant values that can be determined at compile or link time, and their type must be
- An integer or enumeration type (most common)
- A pointer or pointer-to-member type
- std::nullptr_t
- And a couple of other things...

**Template-Template Parameters**
Template parameters can themselves be templates
- Placeholders for class or alias templates
- Declared like class templates, but only the class and typename keywords can be used
```c++
#include <vector>
#include <list>

template<class T, template<class U, class A = std::allocator<U>> class C>
struct Adaptor
{
    C<T> my_data;
    void push_back(T const& t) { my_data.push_back(t); }
};
Adaptor<int, std::vector> a1;
Adaptor<long, std::list> a2;
a1.push_back(0);
a2.push_back(1);
```

**Default Template Arguments**
Template parameters can have default arguments
```c++
template<class T, class Alloc = allocator<T>>
class vector {...};

template<class T, size_t N = 32>
class Array {...}

template<class T, template<class U, class A = allocator<U>> class C = vector>
struct Adaptor {...};

vector<double> vec; //- std::vector<double, std::allocator<double>>
Array<long> arr; //- Array<long, 32>
Adaptor<int> adp; //- Adaptor<int, std::vector<int, std::allocator<int>>>
```
Default arguments must occur at the end of the list for class, alias, and variable templates
```c++
template<class T0, class T1=int, class T2=int, class T3=int>
class quad; //- OK
template<class T0, class T1=int, class T2=int, class T3=int, class T4>
class quint; //- Error
```
Function templates don't have this requirement. Template type deduction can determine the template parameters
```c++
template<class RT=void, class T>
RT* address_of(T& value)
{
    return static_cast<RT*>(&value);
};
```
**Substituting Template Arguments for Template Parameters**
- Template parameters are the names that come after the template keyword in a template declaration
- Template arguments are the concrete items substituted for template parameters to create a template specialization

## Specialization vs Instantiation
- The concrete entity resulting from substituting template arguments for template parameters is a specialization
- These entities are named, and the name has the syntactic form template-name<argument-list>
- This name is formally called a template-id
```c++
template<class T1, class T2>
struct pair
{
    T1 first;
    T2 second;
    ...
};

template<class T>
T const& max(T const& a, T const& b)
{ ... }
---

pair<string, double> my_pair;
double d = max<double>(0, 1);
string s1 = ...;
string s2 = ...;
string s3 = max(s1, s2);
```
From the earlier example
- pair is a class template
- max is a function template
From the earlier example
```c++
    pair<string, double>
    max<double>
    max<string>
```
are the names of specializations.

Q: How do we get from template to specialization?
- A1: Instantiation
- A2: Explicit specialization

### Instantiation

- At some point we'll want to use the recipe and make a thing
  - Most of the time the compiler knows how to cook the recipe for us
- At various times, the compiler will **substitute** concrete (actual) template arguments for the template parameters used by a template
- Sometimes this substitution is tentative
- The compiler checks to see if a possible substitution could be valid
- Sometimes the result of this substitution is used to create a specialization

**Template instantiation** occurs when the compiler substitutes template arguments for template parameters in order to define an entity
- i.e., generate a specialization of some template
- The specialization from instantiating a class template is sometimes called
(informally) an instantiated class
- Likewise for the other template categories (instantiated function, etc.)
- These are also informally called **instantiations**

Template instantiation can occur in two possible ways:

- **Implicitly**
- **Explicitly**


## References

Slides are also included in the respective folder in this repository.

- CppCon2021 Back to Basics: Templates by Bob Steagall. [Video](https://www.youtube.com/watch?v=XN319NYEOcE&list=PLHTh1InhhwT4TJaHBVWzvBOYhp27UO7mI&index=13),
[Slides](https://github.com/CppCon/CppCon2021/tree/main/Presentations)

- [Cpp Reference Website](https://en.cppreference.com/w/cpp/language/)