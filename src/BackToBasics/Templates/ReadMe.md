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

Here we user template and then using keywords.

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

An entity gets a name. A name is the use of an identifier that denotes an entity (or label).
Every name that denotes an entity is introduced by a declaration. A declaration introduces one or more names into translation unit. Note that, a declaration can and may *re-introduce* a name into a translation unit.

## Specialization vs Instantiation



## References

CppCon2021 Back to Basics: Templates by Bob Steagall. [Video](https://www.youtube.com/watch?v=XN319NYEOcE&list=PLHTh1InhhwT4TJaHBVWzvBOYhp27UO7mI&index=13),
[Slides](https://github.com/CppCon/CppCon2021/tree/main/Presentations)

Slides are also included in the respective folder in this repository.