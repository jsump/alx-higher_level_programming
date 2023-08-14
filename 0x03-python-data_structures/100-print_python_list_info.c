#include <Python.h>
/**
* print_python_list_info
* @p: pointer to object
* Return: void
*/
void print_python_list_info(PyObject *p)
{
	int size = PyList_Size(p);
	printf("[*] Size of the Python List = %d\n", size);

	int allocated = ((PyListObject *)p)->allocated;
	printf("[*] Allocated = %d\n", allocated);

	for (int i = 0; i < size; i++)
	{
		PyObject *item = PyList_GetItem(p, i);
		const char *type = item->ob_type->tp_name;
		printf("Element %d: %s\n", i, type);
	}
}
