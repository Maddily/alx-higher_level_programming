#include <Python.h>

/**
 * print_python_bytes - Prints basic info about Python bytes objects
 *
 * @p: A pointer to an object
*/
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	const char *string;
	PyBytesObject *bytes_object;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	bytes_object = (PyBytesObject *)p;
	size = PyBytes_Size(p);
	string = bytes_object->ob_sval;

	printf("  size: %ld\n", size);
	printf("  trying string: %s\n", string);
	printf("  first %d bytes: ", size > 10 ? 10 : (int)(size + 1));

	for (i = 0; i < (size > 10 ? 10 : size); i++)
	{
		if (i == 9 && size >= 10)
			printf("%02x", (unsigned char)string[i]);
		else
			printf("%02x ", (unsigned char)string[i]);
	}
	if (size < 10)
		printf("00");
	printf("\n");
}
/**
 * print_python_list - Prints basic info about Python lists
 *
 * @p: A pointer to an object
*/
void print_python_list(PyObject *p)
{
	const char *unicode_string;
	ssize_t size, i;
	PyListObject *list;
	PyObject *item;

	list = (PyListObject *)p;
	size = list->ob_base.ob_size;

	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %ld: ", i);

		if (PyBytes_Check(item))
		{
			printf("bytes\n");
			print_python_bytes(item);
		}
		else if (PyUnicode_Check(item))
		{
			unicode_string = PyUnicode_AsUTF8(item);
			printf("str\n  trying string: %s\n", unicode_string);
		}
		else
		{
			printf("Element %ld: %s\n", i, list->ob_item[i]->ob_type->tp_name);
		}
	}
}
