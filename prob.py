import random


class Hat:
    def __init__(self, **kwargs):
        self.value_list = []

        for keys in kwargs.keys():
            for i in range(kwargs[keys]):
                self.value_list.append(keys)

    def draw(self, number):
        return random.sample(self.value_list, number)


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    """hat: A hat object containing balls that should be copied inside the function.
expected_balls: An object indicating the exact group of balls to attempt to draw from
the hat for the experiment. For example, to determine the probability of drawing 2 blue
balls and 1 red ball from the hat, set expected_balls to {"blue":2, "red":1}.
num_balls_drawn: The number of balls to draw out of the hat in each experiment.
num_experiments: The number of experiments to perform. (The more experiments performed,
the more accurate the approximate probability will be.)"""

    count = 0

    for i in range(num_experiments):
        draw_list = hat.draw(num_balls_drawn)
        draw_dict = {}

        for color in draw_list:
            try:
                draw_dict[color] += 1
            except:
                draw_dict[color] = 1

        temp_count = 0
        for key in expected_balls.keys():
            try:
                if draw_dict[key] >= expected_balls[key]:
                    temp_count += 1
            except:
                continue


        # print(draw_dict)
        # print(temp_count)

        if temp_count == len(expected_balls):
            count += 1

    # print(count)

    return count / num_experiments


hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                         expected_balls={"red":2,"green":1},
                         num_balls_drawn=5,
                         num_experiments=2000)

print(probability)




