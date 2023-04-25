# src

add_s

add_executable(main main.cc)

install(TARGETS main DESTINATION "."
        RUNTIME DESTINATION bin
        ARCHIVE DESTINATION lib
        LIBRARY DESTINATION lib
        )