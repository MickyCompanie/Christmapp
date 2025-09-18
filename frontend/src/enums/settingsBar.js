import { GiftIcon, ShoppingCartIcon, UserIcon } from '@heroicons/vue/24/solid'

export const settingsBar = [
    {
        title: "gift status",
        routeName: "giftStatusList",
        icon: GiftIcon,
    },
    {
        title: "groceries status",
        routeName: "groceriesStatusList",
        icon: ShoppingCartIcon,
    },
    {
        title: "users",
        routeName: "userList",
        icon: UserIcon,
    },
]