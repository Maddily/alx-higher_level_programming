#include <Python.h>

/**
 * print_python_string - Prints Python strings
 *
 * @p: A pointer to a Python object
*/
void print_python_string(PyObject *p)
{
	const char *string_type;
	Py_ssize_t string_length;
	const wchar_t *string;

	setbuf(stdout, NULL);

	printf("[.] string object info\n");

	if (!PyUnicode_Check(p))
		printf("  [ERROR] Invalid String Object\n");
	else
	{
		string_type = (PyUnicode_IS_COMPACT_ASCII(p)) ?
		"compact ascii" : "compact unicode object";

		string_length = PyUnicode_GET_LENGTH(p);

		string = PyUnicode_AsWideCharString(p, &string_length);

		printf("  type: %s\n", string_type);
		printf("  length: %zd\n", string_length);
		printf("  value: %ls\n", string);

		PyMem_Free((void *)string);
	}
}
