#include <Python.h>
void print_python_list_info(PyObject *p)
{
int size = PyList_size(p);
printf("[*] Size of the Python List = %d\n", size);

int allocated = ((PyListObject *)p)->allocated;
printf("[*] Allocated = %d\n", allocated);

for (int = 0; i < size; i++)
{
PyObject *item = PyList_GetItem(p, i);
const char *type = item->ob_type->tp_name;
printf("element %D: %s\n", i, type);
}
}
