#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);
void print_python_float(PyObject *p);

/**
 * print_python_list - Prints basic info about Python lists
 *
 * @p: A pointer to a Python object
*/
void print_python_list(PyObject *p)
{
	PyListObject *list;
	PyObject *element;
	ssize_t i, size = 0;

	setbuf(stdout, NULL);

	printf("[*] Python list info\n");
	if (!PyList_Check(p))
		printf("  [ERROR] Invalid List Object\n");
	else
	{
		list = (PyListObject *)p;

		size = list->ob_base.ob_size;
		printf("[*] Size of the Python List = %ld\n", size);
		printf("[*] Allocated = %ld\n", list->allocated);
		for (i = 0; i < size; ++i)
		{
			if (element != NULL)
			{
				printf("Element %ld: ", i);

				element = list->ob_item[i];

				if (PyBytes_Check(element))
				{
					printf("bytes\n");
					print_python_bytes(element);
				}
				else if (PyFloat_Check(element))
				{
					printf("float\n");
					print_python_float(element);
				}
				else
					printf("%s\n", element->ob_type->tp_name);
			}
		}
	}
}

/**
 * print_python_bytes - Prints basic info about Python byte objects
 *
 * @p: A pointer to a Python object
*/
void print_python_bytes(PyObject *p)
{
	PyBytesObject *bytes_object;
	ssize_t i, size = 0, first_bytes;
	unsigned char byte;

	setbuf(stdout, NULL);

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
		printf("  [ERROR] Invalid Bytes Object\n");
	else
	{
		bytes_object = (PyBytesObject *)p;

		size = bytes_object->ob_base.ob_size;
		printf("  size: %ld\n", size);

		printf("  trying string: ");
		for (i = 0; i < size; ++i)
		{
			byte = bytes_object->ob_sval[i];
			printf("%c", byte);
		}
		printf("\n");

		first_bytes = (size > 10) ? 10 : size;
		printf("  first %ld bytes: ", (first_bytes == 10) ?
		first_bytes : first_bytes + 1);
		for (i = 0; i < size && i < first_bytes; ++i)
		{
			printf("%02x", (unsigned char)bytes_object->ob_sval[i]);
			if (i < first_bytes - 1)
				printf(" ");
		}
		if (size < 10)
			printf(" 00");
		printf("\n");
	}
}

/**
 * print_python_float - Prints basic info about Python float objects
 *
 * @p: A pointer to a Python object
*/
void print_python_float(PyObject *p)
{
	PyFloatObject *float_object;
	double value;

	setbuf(stdout, NULL);

	printf("[.] float object info\n");
	if (!PyFloat_Check(p))
		printf("  [ERROR] Invalid Float Object\n");
	else
	{
		float_object = (PyFloatObject *)p;
		value = float_object->ob_fval;

		printf("  value: %.1f\n", value);
	}
}
