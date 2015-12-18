#!/usr/bin/env python
# -*- coding: utf-8 -*-


class PressLogic:
    def __init__(self):
        """
        +set_current_step - устанавливает свойства
        self._left_current_images
        self._right_current_images
        self._current_method

        +set_condition_step - меняет свойства согласно контексту

        +left_press > return :str возвр. имя метода (что делать)
        name имя объекта изображения
        +right_press > return :str возвр. имя метода (что делать)
        name имя объекта изображения
        """
        self._right_img_name = None
        self._left_img_name = None
        self._left_current_images = []
        self._right_current_images = []
        # имя метода который надо вызвать при текущем состоянии
        self._current_method = ""

        self.methods_name_next = {"_no_action": self._no_action,
                             "_sort_game": self._sort_game,
                             "_revers_game": self._revers_game}

        self.methods_name_press = {"_no_action": self._no_action_press,
                              "_sort_game": self._sort_game_press,
                              "_revers_game": self._revers_game_press}

        # ---------- интерфейс ------------------------------------->>>

    def set_current_step(self, left_images, right_images,
                         metod_press):
        """

        :param left_images: list имена фото с левой стороны (str)
        :param right_images: list
        :param metod_press: str имя метода который вызывается при
        нажатии next (на экране появляются объекты изображений)
        эти методы что то делают со списком имён этих изображений
        например сортируют
        """
        self._set_left_images(*left_images)
        self._set_right_images(*right_images)
        self._set_current_method(metod_press)

    def set_condition_step(self):

        """
        установить состояние шага
        вызывает один из методов self.methods_next
        """
        self.methods_name_next[self._get_current_method]()

    def left_press(self, name):
        return self.methods_name_press[self._get_current_method](name,
                                                            "left")

    def right_press(self, name):
        self._set_right_img_name(name)
        return self.methods_name_press[self._get_current_method](name,
                                                            "right")

    # -----------------------------------------------------------------

    def _set_right_img_name(self, press_name):
        self._right_img_name = press_name

    @property
    def _get_right_img_name(self):
        return self._right_img_name

    def _set_left_images(self, *images):
        self._left_current_images.clear()
        self._left_current_images = list(images)

    @property
    def _get_left_image_and_del(self):
        return self._left_current_images.pop()

    def _set_right_images(self, *images):
        self._right_current_images.clear()
        self._right_current_images = list(images)

    @property
    def _get_right_images(self):
        return self._right_current_images

    def _set_current_method(self, method):
        self._current_method = method

    @property
    def _get_current_method(self):
        return self._current_method

    # -----------------------------------------------------------------

    # методы подготавливают (формируют) списки имён для дальнейшего
    # использования


    def _sort_game(self):
        self._left_current_images.sort(reverse=True)
        self._left_current_images.pop(0)

    def _no_action(self):
        pass

    def _revers_game(self):
        self._left_current_images.sort(reverse=True)

    # -----------------------------------------------------------------
    # вызываются при нажатии на объект изображения
    # возвращают:
    #           имя метода :str
    #           имя изображения str
    #           имя окна (left, right) на котором была нажата кнопка

    def _no_action_press(self, name, side):
        return "none", name, side

    def _sort_game_press(self, name, side):
        if side == "right":
            return "select_image", name, side
        else:
            pop_img = int(self._get_left_image_and_del)
            right = self._get_right_img_name
            if right is None:
                return "none", name, side
            else:
                right = int(right)
            name = int(name)
            if (-right == pop_img == name):
                return "move_right_to_left", name, side
            else:
                return "reset_game", name, side

    def _revers_game_press(self, name, side):
        return "revers"


if __name__ == '__main__':
    pass
