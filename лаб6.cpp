АЛГОРИТМЫ СОРТИРОВКИ

СОРТИРОВКА ВЫБОРОМ (SELECTION SORT)

cpp
#include <iostream>
using namespace std;

// Функция сортировки массива методом выбора
void selectionSort(int arr[], int n) {
    for (int i = 0; i < n - 1; i++) {
        int minIndex = i; // считаем текущий элемент минимальным
        // ищем минимальный элемент в оставшейся неотсортированной части
        for (int j = i + 1; j < n; j++) {
            if (arr[j] < arr[minIndex]) {
                minIndex = j;
            }
        }
        // обмен текущего элемента с найденным минимумом
        swap(arr[i], arr[minIndex]);
    }
}

// Вывод массива на экран
void printArray(const int arr[], int n) {
    for (int i = 0; i < n; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;
}

int main() {
    const int SIZE = 5;
    int arr[SIZE] = {64, 25, 12, 22, 11};

    cout << "Исходный массив:" << endl;
    printArray(arr, SIZE);

    selectionSort(arr, SIZE);

    cout << "Отсортированный массив:" << endl;
    printArray(arr, SIZE);

    return 0;
}
Исходный массив:
64 25 12 22 11
Отсортированный массив:
11 12 22 25 64

СОРТИРОВКА СЛИЯНИЕМ (MERGE SORT)

cpp
#include <iostream>
#include <vector>
using namespace std;

// Объединение двух отсортированных частей массива
void merge(vector<int>& arr, int left, int mid, int right) {
    int n1 = mid - left + 1;
    int n2 = right - mid;

    vector<int> L(n1), R(n2);
    for (int i = 0; i < n1; i++) L[i] = arr[left + i];
    for (int j = 0; j < n2; j++) R[j] = arr[mid + 1 + j];

    int i = 0, j = 0, k = left;

    // объединяем обе половины в единый массив
    while (i < n1 && j < n2) {
        if (L[i] <= R[j]) arr[k++] = L[i++];
        else arr[k++] = R[j++];
    }

    // добавляем оставшиеся элементы
    while (i < n1) arr[k++] = L[i++];
    while (j < n2) arr[k++] = R[j++];
}

// Рекурсивная функция сортировки
void mergeSort(vector<int>& arr, int left, int right) {
    if (left < right) {
        int mid = left + (right - left) / 2;
        mergeSort(arr, left, mid);
        mergeSort(arr, mid + 1, right);
        merge(arr, left, mid, right);
    }
}

// Вывод на экран
void printArray(const vector<int>& arr) {
    for (int num : arr) cout << num << " ";
    cout << endl;
}

int main() {
    vector<int> arr = {38, 27, 43, 3, 9, 82, 10};

    cout << "Исходный массив: ";
    printArray(arr);

    mergeSort(arr, 0, arr.size() - 1);

    cout << "Отсортированный массив: ";
    printArray(arr);

    return 0;
}
Исходный массив: 38 27 43 3 9 82 10
Отсортированный массив: 3 9 10 27 38 43 82

ПИРАМИДАЛЬНАЯ СОРТИРОВКА (HEAP SORT)

cpp
#include <iostream>
#include <vector>
using namespace std;

// Восстановление свойств кучи
void heapify(vector<int>& arr, int n, int root) {
    int largest = root;
    int left = 2 * root + 1;
    int right = 2 * root + 2;

    if (left < n && arr[left] > arr[largest]) largest = left;
    if (right < n && arr[right] > arr[largest]) largest = right;

    if (largest != root) {
        swap(arr[root], arr[largest]);
        heapify(arr, n, largest);
    }
}

// Основная функция сортировки
void heapSort(vector<int>& arr) {
    int n = arr.size();

    // строительство max-кучи
    for (int i = n / 2 - 1; i >= 0; i--) heapify(arr, n, i);

    // извлечение элементов из кучи
    for (int i = n - 1; i > 0; i--) {
        swap(arr[0], arr[i]);
        heapify(arr, i, 0);
    }
}

// Печать массива
void printArray(const vector<int>& arr) {
    for (int v : arr) cout << v << " ";
    cout << endl;
}

int main() {
    vector<int> arr = {12, 11, 13, 5, 6, 7};

    cout << "Исходный массив: ";
    printArray(arr);

    heapSort(arr);

    cout << "Отсортированный массив: ";
    printArray(arr);

    return 0;
}
Исходный массив: 12 11 13 5 6 7
Отсортированный массив: 5 6 7 11 12 13

АЛГОРИТМЫ ПОИСКА

БИНАРНЫЙ (ДВОИЧНЫЙ) ПОИСК

cpp
#include <iostream>
#include <vector>
using namespace std;

// Функция бинарного поиска
int binarySearch(const vector<int>& arr, int target) {
    int low = 0;
    int high = arr.size() - 1;

    while (low <= high) {
        int mid = low + (high - low) / 2;

        if (arr[mid] == target)
            return mid;
        else if (arr[mid] < target)
            low = mid + 1;
        else
            high = mid - 1;
    }
    return -1;
}

int main() {
    vector<int> arr = {2, 3, 4, 10, 40};
    int target = 10;

    int result = binarySearch(arr, target);

    if (result != -1)
        cout << "Элемент найден на позиции: " << result << endl;
    else
        cout << "Элемент не найден." << endl;

    return 0;
}
Элемент найден на позиции: 3

ИНТЕРПОЛИРУЮЩИЙ ПОИСК

cpp
#include <iostream>
#include <vector>
using namespace std;

// Функция интерполирующего поиска
int interpolationSearch(const vector<int>& arr, int target) {
    int low = 0;
    int high = arr.size() - 1;

    while (low <= high && target >= arr[low] && target <= arr[high]) {
        int pos = low + ((double)(high - low) /
                        (arr[high] - arr[low])) * (target - arr[low]);

        if (arr[pos] == target)
            return pos;

        if (arr[pos] < target)
            low = pos + 1;
        else
            high = pos - 1;
    }
    return -1;
}

int main() {
    vector<int> arr = {10, 12, 13, 16, 18, 19, 20, 21, 22, 23, 24, 33, 35, 42, 47};
    int target = 18;

    int result = interpolationSearch(arr, target);

    if (result != -1)
        cout << "Элемент найден на позиции: " << result << endl;
    else
        cout << "Элемент не найден." << endl;

    return 0;
}
Элемент найден на позиции: 4
