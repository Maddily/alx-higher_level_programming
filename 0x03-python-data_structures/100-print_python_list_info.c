#include <Python.h>

/**
 * print_python_list_info - Prints some basic info about Python lists
 *
 * @p: A pointer to an object
*/
void print_python_list_info(PyObject *p)
{
	int i;
	ssize_t size;
	PyListObject *list;

	list = (PyListObject *)p;
	size = list->ob_base.ob_size;

	printf("[*] Size of the Python List = %ld\n", list->ob_base.ob_size);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < size; i++)
	{
		printf("Element %d: %s\n", i, list->ob_item[i]->ob_type->tp_name);
	}
}
