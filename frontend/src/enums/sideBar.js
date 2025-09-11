import { GiftIcon, ShoppingCartIcon, SparklesIcon } from '@heroicons/vue/24/solid'

export const sideBar = [
    {
        title: "wishes",
        routeName: "wisheslist",
        icon: SparklesIcon,
    },
    {
        title: "gifts",
        routeName: "giftlist",
        icon: GiftIcon,
    },
    {
        title: "groceries",
        routeName: "grocerieslist",
        icon: ShoppingCartIcon,
    },
]