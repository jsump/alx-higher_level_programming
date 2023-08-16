#include <Python.h>
#include <stdio.h>
/**
 * print_python_list - print information about python lists
 * @p: pointer to first item on list
 */
void print_python_list(PyObject *p)
{
	Py_ssize_t size, i;
	PyObject *item;

	printf("[*] Python list information\n");

	if (!PyList_check(p))
	{
		printf("[ERROR] Invalid List Object\n");
		return;
	}
	size = PyList_Size(p);
	printf("[*] Size of the Python List = %zd\n", size);
	printf("[*] Allocated = %d\n", ((PyLostObject *)p)->allocated);

	for (i = 0; i < size; i++)
	{
		item = PyList_GetItem(p, i);
		printf("Element %zd: %s\n", i, Py_TYPE(item)->tp_name);
	}
}
void print_python_bytes(PyObject *p)
{
	Py_ssize_t size, i;
	char *buffer;

	printf("[*] Python bytes information\n");
	if (!PyBytes_Check(p))
	{
		printf(" [ERROR] Invalid Bytes Object\n");
		return;
	}
	size = PyBytes_Size(p);
	printf(" Size: %zd\n", size);
	buffer = PyBytes_AsString(p);
	printf(" Trying string: %s\n", buffer != NULL ? buffer : "(null)");

	printf(" First %zd bytes: ", size < 10 ? size + 1 : 10);

	for ( i = 0; i < size && i < 10; i++)
	{
		printf("%02hhx%c", buffer[i], i ==9 ? '\n' : ' ' );
	}
}
