from dataclasses import dataclass, fields
import tkinter as tk
from tkinter import ttk


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


def main():
    brandNames = ["AMD", "Zommer", "Manover", "Original", "TORK"]
    materials = ["Материал 1", "Материал 2", "Материал 3", "Материал 4"]
    marks = ["Без маркировки", "AMD", "Zommer", "Manover", "TORK"]
    boxMarks = ["NONAME", "AMD", "Zommer", "Manover", "TORK", "Original"]
    groupBoxMarks = ["NONAME", "AMD", "Manover", "TORK"]
    itemTypes = [ItemType("Ролик приводного ремня"), ItemType("Расширительный бачок")]
    subItemTypes = [SubItemType("Подшипник")]
    subItems = [SubItem(subItemTypes[0], "NONAME"), SubItem(subItemTypes[0], "KRAFT")]
    brands = [
        Brand(
            brandNames[0],
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
            brandNames[1],
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
            brandNames[2],
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
            brandNames[3],
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
            brandNames[4],
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
    window.columnconfigure(2, minsize=800, weight=1)
    fr_brand = tk.Frame(window, relief=tk.RAISED, bd=2)
    fr_item = tk.Frame(window, relief=tk.RAISED, bd=2)

    def selectedBrand(event):
        currentBrand = cb_brand.get()
        cb_item["values"] = [it.name for it in itemTypes]
        cb_item["state"] = "readonly"

    lb_brand = tk.Label(fr_brand, text="Выберите фирму", height=3, width=30)
    cb_brand = ttk.Combobox(fr_brand, values=brandNames, state="readonly")
    cb_brand.bind("<<ComboboxSelected>>", selectedBrand)

    def selectedItem(event):
        selection = cb_item.get()
        window.title(selection)

    lb_item = tk.Label(fr_item, text="Номенклатура", height=3, width=30)
    cb_item = ttk.Combobox(
        fr_item,
        values=[],
        state="disabled",
    )
    cb_item.bind("<<ComboboxSelected>>", selectedItem)

    fr_brand.grid(row=0, column=0, sticky="ns", padx=5, pady=5)
    lb_brand.grid(row=0, column=0, sticky="ew", padx=2, pady=2)
    cb_brand.grid(row=1, column=0, sticky="ew", padx=2, pady=2)

    fr_item.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)
    lb_item.grid(row=0, column=1, sticky="ew", padx=2, pady=2)
    cb_item.grid(row=1, column=1, sticky="ew", padx=2, pady=2)
    window.mainloop()


if __name__ == "__main__":
    main()
