#include <Python.h>
#include <stdio.h>

/**
 * print_python_float - ..
 * @p: ..
 * Return: 0
 */
void print_python_float(PyObject *p)
{
	double value = 0;
	char *string = NULL;

	fflush(stdout);
	printf("[.] float object info\n");

	if (!PyFloat_CheckExact(p))
	{
		printf("  [ERROR] Invalid Float Object\n");
		return;
	}

	value = ((PyFloatObject *)p)->ob_fval;
	string = PyOS_double_to_string(value, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
	printf("  value: %s\n", string);
}
/**
 * print_python_bytes - ..
 * @p: ..
 * Return: 0
 */
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size = 0;
	char *string = NULL;

	fflush(stdout);
	printf("[.] bytes object info\n");

	if (!PyBytes_CheckExact(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	size = PyBytes_Size(p);
	printf("  size: %zd\n", size);
	string = ((PyBytesObject *)(p))->ob_sval;
	printf("  trying string: %s\n", string);
	printf("  first %zd bytes:", size < 10 ? size : 10);

	for (Py_ssize_t a = 0; a < size && a < 10; a++)
	{
		printf(" %02hhx", string[a]);
	}
	printf("\n");
}
/**
 * print_python_list - ....
 * @p: ....
 * Return: 0
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size = 0;
	PyObject *item;

	fflush(stdout);
	printf("[*] Python list info\n");

	if (PyList_CheckExact(p))
	{
		size = PyList_GET_SIZE(p);
		printf("[*] Size of the Python List = %zd\n", size);
		printf("[*] Allocated = %lu\n", ((PyListObject *)p)->allocated);

		for (Py_ssize_t a = 0; a < size; a++)
		{
			item = PyList_GET_ITEM(p, a);
			printf("Element %zd: %s\n", a, item->ob_type->tp_name);

			if (PyBytes_Check(item))
			{
				print_python_bytes(item);
			}
			else if (PyFloat_Check(item))
			{
				print_python_float(item);
			}
		}
	}
	else
	{
		printf("  [ERROR] Invalid List Object\n");
	}
}

