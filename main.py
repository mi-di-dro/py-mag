from dataclasses import dataclass
import tkinter as tk


def main():
    materials = ["Материал 1", "Материал 2", "Материал 3", "Материал 4"]
    marks = ["Без маркировки", "AMD", "Zommer", "Manover", "TORK"]
    boxMarks = ["NONAME", "AMD", "Zommer", "Manover", "TORK", "Original"]
    groupBoxMarks = ["NONAME", "AMD", "Manover", "TORK"]
    itemTypes = [ItemType("Ролик приводного ремня"), ItemType("Расширительный бачок")]
    subItemTypes = [SubItemType("Подшипник")]
    subItems = [SubItem(subItemTypes[0], "NONAME"), SubItem(subItemTypes[0], "KRAFT")]
    brands = [
        Brand(
            "AMD",
            [
                Item(
                    itemTypes[0],
                    [subItems[0]],
                    materials[0],
                    marks[1],
                    boxMarks[1],
                    groupBoxMarks[1],
                ),
                Item(
                    itemTypes[1],
                    [],
                    materials[2],
                    marks[1],
                    boxMarks[1],
                    groupBoxMarks[1],
                ),
            ],
        ),
        (
            "Zommer",
            [
                Item(
                    itemTypes[0],
                    [subItems[0]],
                    materials[1],
                    marks[2],
                    boxMarks[2],
                    groupBoxMarks[0],
                ),
                Item(
                    itemTypes[1],
                    [],
                    materials[2],
                    marks[0],
                    boxMarks[0],
                    groupBoxMarks[0],
                ),
            ],
        ),
        (
            "Manover",
            [
                Item(
                    itemTypes[0],
                    [subItems[1]],
                    materials[0],
                    marks[3],
                    boxMarks[3],
                    groupBoxMarks[2],
                ),
                Item(
                    itemTypes[1],
                    [],
                    materials[2],
                    marks[3],
                    boxMarks[3],
                    groupBoxMarks[2],
                ),
            ],
        ),
        (
            "Original",
            [
                Item(
                    itemTypes[0],
                    [subItems[1]],
                    materials[1],
                    marks[0],
                    boxMarks[5],
                    groupBoxMarks[0],
                ),
                Item(
                    itemTypes[1],
                    [],
                    materials[3],
                    marks[0],
                    boxMarks[0],
                    groupBoxMarks[0],
                ),
            ],
        ),
        (
            "TORK",
            [
                Item(
                    itemTypes[0],
                    [subItems[1]],
                    materials[0],
                    marks[0],
                    boxMarks[4],
                    groupBoxMarks[3],
                ),
                Item(
                    itemTypes[1],
                    [],
                    materials[3],
                    marks[4],
                    boxMarks[4],
                    groupBoxMarks[3],
                ),
            ],
        ),
    ]

    window = tk.Tk()
    window.title("Производство и упаковка товара")
    window.rowconfigure(0, minsize=800, weight=1)
    window.columnconfigure(1, minsize=800, weight=1)

    label = tk.Label(text="Test text")
    label.pack()

    window.mainloop()


if __name__ == "__main__":
    main()


@dataclass
class Material:
    name: str


@dataclass
class Mark:
    name: str


@dataclass
class BoxMark:
    name: str


@dataclass
class GroupBoxMark:
    name: str


@dataclass
class SubItemType:
    name: str


@dataclass
class SubItem:
    type: SubItemType
    name: str


@dataclass
class ItemType:
    name: str


@dataclass
class Item:
    type: ItemType
    subitems: list[SubItem]
    material: Material
    mark: Mark
    boxMark: BoxMark
    groupBoxMark: GroupBoxMark


@dataclass
class Brand:
    name: str
    items: list[Item]
