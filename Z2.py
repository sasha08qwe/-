def calculate_total_burn_time(c1):
    if c1 == 0:
        return 0

    # Время горения одного огонька
    burn_time_per_firework = 2

    # Потухшие огоньки можно использовать для создания новых
    new_fireworks = c1 // 1  # Из каждого потухшего огонька можно сделать 2 новых

    # Рекурсивно вычисляем время горения огоньков
    total_burn_time = c1 * burn_time_per_firework + calculate_total_burn_time(new_fireworks)

    return total_burn_time


# Пример использования
c1 = 1  # Количество начальных бенгальских огней
total_burn_time = calculate_total_burn_time(c1)
print(f"Общее время горения огоньков: {total_burn_time} часов")
