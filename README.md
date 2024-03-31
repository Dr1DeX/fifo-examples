# fifo-examples
![workflow](https://github.com/Dr1DeX/fifo-examples/actions/workflows/main.yml/badge.svg)
## Пример реализации двух абстракций FIFO: различия, преимущества и недостатки.

________________

### Мы имеем две реализации очереди основанный на кольцевом буфере: Классическая односторонняя очередь(Queue) и двухсторонняя очередь(Deque)

________________

### Классическая очередь(Queue):
#### Ее принцип работы противоположен абстрактному интерфейсу LIFO, т.е элемент будет извлечен в порядке очереди(кто раньше, тот и будет раньше обработан) 


        def push(self, x):
            if self.size != self.max_size:
                self.queue[self.tail] = x
                self.tail = (self.tail + 1) % self.max_size
                self.size += 1

        def pop(self):
            try:
                if self.is_empty():
                    raise EmptyArrException
                x = self.queue[self.head]
                self.queue[self.head] = None
                self.head = (self.head + 1) % self.max_size
                return x
            except EmptyArrException:
                print('error: empty queue')


### Преимущества:
#### 1) Ключевые методы вставки и извлечения(``push`` и ``pop``) имеют асимптотическую сложность по времени `O(1)`, что позволяет эффективно обрабатывать данные(в том числе и потоковые)
#### 2) Простота в интеграции. Поскольку FIFO в целом это не какая-то конкретная структура данных, а лишь набор правил и рекомендаций по организации структуры данных, мы можем с легкостью сделать свою собственную имплементацию в зависимости от специфики и бизнес-логики проекта.

### Недостатки:
#### 1)Кольцевой буфер сам по себе имеет фиксированный размер и ее превышение может грохнуть программу, конечно, в Python проблемы с переполнением не возникнет, но в других ЯП это нужно иметь виду.
#### P.S Конкретно в питоне может возникнуть релокация массива, копирования старого участка памяти в новую может стоить дорого.

#### 2) Race condition('Гонка данных'), может получиться так, что процессы скорости обработки потоковых данных и операции чтения имеют разную скорость, и тогда мы получим блокирующую очередь или потерю данных :) 

-----------

### Двухсторонняя очередь(Deque)
#### По сути это модификация однонаправленной очереди.
### Преимущества:
#### Главное преимущество в том, что мы можем организовать данные не только как FIFO(положить в начало и достать из начала), но и работать как с LIFO(положить в конец, достать из начала), что делает его более удобным и универсальным

        def push(self, x):
            if self.__is_full_queue():
                raise FullArrException
            elif self.is_empty():
                self.front_q = 0
                self.back_q = 0
                self.queue[self.front_q] = x
            else:
                self.front_q = (self.front_q - 1 + self.max_size) % self.max_size
                self.queue[self.front_q] = x

        def push_back(self, x):
            if self.__is_full_queue():
                raise FullArrException
            elif self.is_empty():
                self.front_q = 0
                self.back_q = 0
                self.queue[self.back_q] = x
            else:
                self.back_q = (self.back_q + 1) % self.max_size
                self.queue[self.back_q] = x

        def pop(self):
            if self.is_empty():
                raise EmptyArrException
            elif self.front_q == self.back_q:
                x = self.queue[self.front_q]
                self.front_q = -1
                self.back_q = -1
                return x
            else:
                x = self.queue[self.front_q]
                self.front_q = (self.front_q + 1) % self.max_size
                return x

        def pop_back(self):
            if self.is_empty():
                raise EmptyArrException
            elif self.front_q == self.back_q:
                x = self.queue[self.back_q]
                self.front_q = -1
                self.back_q = -1
                return x
            else:
                x = self.queue[self.back_q]
                self.back_q = (self.back_q - 1 + self.max_size) % self.max_size
                return x

### Сложность по времени ставки и извлечения будет то же самое - ``O(1)``

### Недостатки:
#### Тут требуется аккуратное управление индексами начала и конца буфера, что усложняет управлению памятью в целом.

----------

## Developer: Dr1DeX