from dataclasses import dataclass
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo


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
    materials = [
        Material("Материал 1"),
        Material("Материал 2"),
        Material("Материал 3"),
        Material("Материал 4"),
    ]
    marks = [
        Mark("Без маркировки"),
        Mark("AMD"),
        Mark("Zommer"),
        Mark("Manover"),
        Mark("TORK"),
    ]
    boxMarks = [
        BoxMark("NONAME"),
        BoxMark("AMD"),
        BoxMark("Zommer"),
        BoxMark("Manover"),
        BoxMark("TORK"),
        BoxMark("Original"),
    ]
    groupBoxMarks = [
        GroupBoxMark("NONAME"),
        GroupBoxMark("AMD"),
        GroupBoxMark("Manover"),
        GroupBoxMark("TORK"),
    ]
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
        Brand(
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
        Brand(
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
        Brand(
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
        Brand(
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

    current_item = None
    current_brand = None

    window = tk.Tk()
    window.title("Производство и упаковка товара")
    window.rowconfigure(0, minsize=400, weight=1)
    window.columnconfigure(2, minsize=400, weight=1)
    fr_brand = tk.Frame(window, relief=tk.RAISED, bd=2)
    fr_item = tk.Frame(window, relief=tk.RAISED, bd=2)
    fr_props = tk.Frame(window, relief=tk.RAISED, bd=2)

    def selectedBrand(event):
        global current_brand
        global current_item
        current_brand = brands[
            [i for i, x in enumerate(brands) if x.name == cb_brand.get()][0]
        ]
        cb_item.set("")
        cb_item["values"] = [it.type.name for it in current_brand.items]
        cb_item["state"] = "readonly"
        btn_material["state"] = "disabled"
        btn_subItems["state"] = "disabled"
        btn_mark["state"] = "disabled"
        btn_boxMark["state"] = "disabled"
        btn_groupBoxMark["state"] = "disabled"
        current_item = None

    lb_brand = tk.Label(fr_brand, text="Выберите фирму", height=3, width=50)
    cb_brand = ttk.Combobox(fr_brand, values=brandNames, state="readonly")
    cb_brand.bind("<<ComboboxSelected>>", selectedBrand)

    def selectedItem(event):
        global current_item
        global current_brand
        current_item = [
            it for it in current_brand.items if it.type.name == cb_item.get()
        ][0]
        btn_material["state"] = "active"
        btn_subItems["state"] = "active"
        btn_mark["state"] = "active"
        btn_boxMark["state"] = "active"
        btn_groupBoxMark["state"] = "active"

    def click_btn_material():
        global current_item
        showinfo(title="Необходимый материал", message=current_item.material.name)

    def click_btn_subItems():
        global current_item
        sub_items = [
            ("Тип детали: " + si.type.name + "  " + "Марка: " + si.name)
            for si in current_item.subitems
        ]

        showinfo(
            title="Необходимые детали",
            message="Нет других деталей в составе"
            if len(sub_items) == 0
            else "\n".join(sub_items),
        )

    def click_btn_mark():
        global current_item
        showinfo(title="Необходимая маркировка", message=current_item.mark.name)

    def click_btn_boxMark():
        global current_item
        showinfo(
            title="Необходимая индивидуальная маркировка",
            message=current_item.boxMark.name,
        )

    def click_btn_groupBoxMark():
        global current_item
        showinfo(
            title="Необходимая групповая маркировка",
            message=current_item.groupBoxMark.name,
        )

    lb_item = tk.Label(fr_item, text="Номенклатура", height=3, width=50)
    cb_item = ttk.Combobox(
        fr_item,
        values=[],
        state="disabled",
    )
    cb_item.bind("<<ComboboxSelected>>", selectedItem)

    lb_props = tk.Label(fr_props, text="Параметры", height=3, width=50)
    btn_material = tk.Button(
        fr_props, text="Материал", command=click_btn_material, state="disabled"
    )
    btn_subItems = tk.Button(
        fr_props, text="Детали в составе", command=click_btn_subItems, state="disabled"
    )
    btn_mark = tk.Button(
        fr_props, text="Маркировка", command=click_btn_mark, state="disabled"
    )
    btn_boxMark = tk.Button(
        fr_props,
        text="Индивидуальная упаковка",
        command=click_btn_boxMark,
        state="disabled",
    )
    btn_groupBoxMark = tk.Button(
        fr_props,
        text="Групповая упаковка",
        command=click_btn_groupBoxMark,
        state="disabled",
    )

    fr_brand.grid(row=0, column=0, sticky="ns", padx=5, pady=5)
    lb_brand.grid(row=0, column=0, sticky="ew", padx=2, pady=2)
    cb_brand.grid(row=1, column=0, sticky="ew", padx=2, pady=2)

    fr_item.grid(row=0, column=1, sticky="ns", padx=5, pady=5)
    lb_item.grid(row=0, column=1, sticky="ew", padx=2, pady=2)
    cb_item.grid(row=1, column=1, sticky="ew", padx=2, pady=2)

    fr_props.grid(row=0, column=2, sticky="nsew", padx=5, pady=5)
    lb_props.grid(row=0, column=2, sticky="ew", padx=2, pady=2)
    btn_material.grid(row=1, column=2, sticky="ew", padx=2, pady=2)
    btn_subItems.grid(row=2, column=2, sticky="ew", padx=2, pady=2)
    btn_mark.grid(row=3, column=2, sticky="ew", padx=2, pady=2)
    btn_boxMark.grid(row=4, column=2, sticky="ew", padx=2, pady=2)
    btn_groupBoxMark.grid(row=5, column=2, sticky="ew", padx=2, pady=2)

    window.mainloop()


if __name__ == "__main__":
    main()
