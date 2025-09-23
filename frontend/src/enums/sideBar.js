import { GiftIcon, ShoppingCartIcon, SparklesIcon, UserGroupIcon ,AdjustmentsHorizontalIcon } from '@heroicons/vue/24/solid'

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
        title: "people",
        routeName: "personlist",
        icon: UserGroupIcon,
    },
    {
        title: "groceries",
        routeName: "grocerieslist",
        icon: ShoppingCartIcon,
    },
]

export  const sideBarSettings = [
    {
        title: "settings",
        routeName: "giftStatusList",
        icon: AdjustmentsHorizontalIcon,
        routeChildren: [
            'giftStatusList',
            'giftStatusCreate',
            'giftStatusEdit',
            'groceriesStatusList',
            'groceriesStatusCreate',
            'groceriesStatusEdit',
            'userList',
        ]
    },
]