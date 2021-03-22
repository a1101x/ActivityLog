from common.enums import ChoiceEnum

from psf.constants import REQUEST_TYPES


class DeviceTypes(ChoiceEnum):
    UNKNOWN = 'Unknown'
    MOBILE = 'Mobile'
    TABLET = 'Tablet'
    DESKTOP = 'Desktop'
    BOT = 'Bot'


class ActionTypes(ChoiceEnum):
    MAIN_SEARCH = 'Main search was performed'
    SEARCH_COMMODITY_CODES = 'Search by commodity codes was performed'
    SEARCH_CONTRACT_VEHICLES = 'Search by contract vehicles was performed'
    USER_CREATED = 'New unverified User has been created'
    EMAIL_VERIFIED = 'User verified email'
    MULTIPLE_ADD_TO_LIST = 'Multiple suppliers saved to list'
    ADD_TO_LIST = 'Supplier saved to list'
    MULTIPLE_REMOVE_FROM_LIST = 'Multiple suppliers removed from list'
    REMOVE_FROM_LIST = 'Supplier removed from list'
    USER_APPROVED = 'User was approved'
    MULTIPLE_EXPORT_TO_PDF = 'Multiple suppliers were exported to PDF'
    COMMODITY_CODES_OPENED = 'Commodity Codes page was opened'
    SEPARATE_COMMODITY_CODE_OPENED = 'Separate Commodity Code was opened'
    CONTRACT_VEHICLES_OPENED = 'Contract Vehicles page was opened'
    SEPARATE_CONTRACT_VEHICLE_OPENED = 'Separate Contract Vehicle page was opened'
    SEPARATE_COMMODITY_CODE_CONTENT = 'Content from Separate Commodity Code was downloaded'
    SEPARATE_CONTRACT_VEHICLE_CONTENT = 'Content from Separate Contract Vehicle was downloaded'
    EXPORT_TO_PDF = 'Supplier is exported to PDF'
    PROFILE_WAS_VIEWED = 'Supplier Profile was viewed'
    SPONSORED_PROFILE_WAS_VIEWED = 'Sponsored Supplier Profile was opened'
    PROFILE_WAS_EDITED = 'Supplier Profile was edited'
    USER_REQUEST_WAS_SENT = 'User Request was sent'
    USER_PROFILE_WAS_OPENED = 'User Profile was opened'
    USER_PROFILE_WAS_EDITED = 'User Profile was edited'
    NOTES_ADDED = 'Notes Added'
    NOTES_EDITED = 'Notes Edited'
    NOTES_DELETED = 'Notes Deleted'
    VERIFICATION_EMAIL_SENT = 'Verification email has been sent'
    MULTIPLE_SHARE_BY_EMAIL = 'Multiple suppliers shared by email'
    SINGLE_SHARE_BY_EMAIL = 'Supplier is shared by email'
    SINGLE_SEND_SUPPLIERS_EMAIL = 'Send email to Single Supplier has been invoked'
    MULTIPLE_SEND_SUPPLIERS_EMAIL = 'Send email to Multiple Suppliers has been invoked'
    FILTER_APPLIED = 'Filter is applied'
    DRAFT_OPPORTUNITY_CREATED = 'Draft Opportunity was created'
    OPPORTUNITY_PUBLISHED = 'Opportunity was published'
    OPPORTUNITIES_OPENED = 'Opportunities page was opened'
    OPPORTUNITY_OPENED = 'View Opportunity page was opened'
    APPLY_OPPORTUNITY = 'APPLY OPPORTUNITY button was clicked'
    SEARCH_OPPORTUNITY = 'Search by opportunities was performed'
    SAVED_LIST_PUBLISHED_BY_USER = 'Saved List was published by user'
    SAVED_LIST_PUBLISHED_ANONYMOUSLY = 'Saved List was published anonymously'
    PUBLIC_SAVED_LIST_COPIED = 'Public Saved List was copied'
    PUBLIC_SAVED_LIST_REMOVED = 'Public Saved List was removed'
    PUBLIC_SAVED_LIST_SHARED = 'Public Saved List was shared'
    SEARCH_PUBLIC_SAVED_LIST = 'Search by Public Lists was performed'
    OPPORTUNITY_LINKED_TO_SAVED_LIST = 'Opportunity was linked to Saved List'
    SUPPLIER_PROFILE_SHARED = 'Supplier Profile was shared'
    COMMODITY_CODE_SHARED = 'Separate Commodity Code page was shared'
    CONTRACT_VEHICLE_SHARED = 'Separate Contract Vehicle page was shared'
    OPPORTUNITY_SHARED = 'Opportunity page was shared'
    VIEW_MODE_CHANGED = 'Suppliers list view was changed'
    PUBLIC_SAVED_LIST_VIEWED = 'Public Saved List was viewed'
    CC_CONNECTED_TO_OPPORTUNITY = 'Commodity Code was connected to Opportunity'
    COVID_SUPPLY_ADDED = 'New COVID-19 Supply was added'
    COVID_SUPPLY_UPDATED = 'Existing COVID-19 Supply was updated'
    MAP_VIEW_SEARCH = 'Suppliers list map view: Search was performed'
    MAP_VIEW_VIEW_CHANGED = 'Suppliers list map view: View mode was changed'
    MAP_VIEW_EXPAND_COLLAPSE = 'Suppliers list map view: All items were expanded or collapsed'
    SUMMARY_REPORT_BUILT = 'Summary Report was built'
    CONTACT_US_OPENED = 'Contact Us page was opened'
    CONTACT_US_FOLLOW_CLICKED = 'Contact Us: Follow was clicked'
    TRAINING_EVENTS_OPENED = 'Training Events page was opened'
    TRAINING_EVENTS_FOLLOW_CLICKED = 'Training Events: Follow was clicked'
    TRAINING_EVENTS_DETAIL_OPENED = 'Training Events: Training Event Details page was opened'
    TRAINING_EVENTS_JOIN = 'Training Events: Join button was clicked'
    TRAINING_EVENTS_DETAIL_FOLLOW = 'Training Event Details: Follow was clicked'
    TRAINING_EVENTS_DETAIL_JOIN = 'Training Event Details: Join button was clicked'
    TRAINING_EVENTS_DETAIL_BACK = 'Training Event Details: Back button was clicked'
    SUPPLIER_CARD_CLICKED = 'Supplier card was clicked'
    LANDING_WAS_OPENED = 'Landing page was opened'
    MAIN_SEARCH_WAS_CLICKED = 'Main search bar was clicked'
    MAIN_SEARCH_WAS_FILLED = 'Main search bar was filled'
    RECENT_SEARCHES_WAS_CLICKED = 'Recent Searches was clicked'
    SEARCH_TYPE_BUTTON_WAS_CLICKED = 'Search Type button was clicked (search for)'
    SEARCH_RESULT_WAS_CLICKED = 'Search result was clicked'
    SHOW_ALL_BUTTON_WAS_CLICKED = 'Show All button was clicked'
    BOTTOM_ALL_ITEMS_BUTTON_WAS_CLICKED = 'Bottom All items button was clicked'
    SUGGESTION_CLOSE_BUTTON_WAS_CLICKED = 'Close button was clicked'
    SEARCH_TYPE_DROPDOWN_WAS_CLICKED = 'Search Type dropdown was clicked'


MULTIPLE_SUPPLIERS = 'multiple'
SINGLE_SUPPLIERS = 'single'
FRONTEND_ACTIONS = {
    'share_by_email': {
        MULTIPLE_SUPPLIERS: ActionTypes.MULTIPLE_SHARE_BY_EMAIL,
        SINGLE_SUPPLIERS: ActionTypes.SINGLE_SHARE_BY_EMAIL,
    },
    'contact_supplier': {
        MULTIPLE_SUPPLIERS: ActionTypes.MULTIPLE_SEND_SUPPLIERS_EMAIL,
        SINGLE_SUPPLIERS: ActionTypes.SINGLE_SEND_SUPPLIERS_EMAIL,
    },
    'filtering': {
        SINGLE_SUPPLIERS: ActionTypes.FILTER_APPLIED,
    },
    'apply_opportunity': {
        SINGLE_SUPPLIERS: ActionTypes.APPLY_OPPORTUNITY,
    },
    'public_saved_list_shared': {
        SINGLE_SUPPLIERS: ActionTypes.PUBLIC_SAVED_LIST_SHARED,
    },
    'change_view': {
        SINGLE_SUPPLIERS: ActionTypes.VIEW_MODE_CHANGED,
    },
    'map_search': {
        SINGLE_SUPPLIERS: ActionTypes.MAP_VIEW_SEARCH,
    },
    'map_change_view': {
        SINGLE_SUPPLIERS: ActionTypes.MAP_VIEW_VIEW_CHANGED,
    },
    'map_expand_collapse': {
        SINGLE_SUPPLIERS: ActionTypes.MAP_VIEW_EXPAND_COLLAPSE,
    },
    'contact_us_follow': {
        SINGLE_SUPPLIERS: ActionTypes.CONTACT_US_FOLLOW_CLICKED,
    },
    'training_events_follow': {
        SINGLE_SUPPLIERS: ActionTypes.TRAINING_EVENTS_FOLLOW_CLICKED,
    },
    'training_event_detail_follow': {
        SINGLE_SUPPLIERS: ActionTypes.TRAINING_EVENTS_DETAIL_FOLLOW,
    },
    'training_events_join': {
        SINGLE_SUPPLIERS: ActionTypes.TRAINING_EVENTS_JOIN,
    },
    'training_event_detail_join': {
        SINGLE_SUPPLIERS: ActionTypes.TRAINING_EVENTS_DETAIL_JOIN,
    },
    'training_event_detail_back': {
        SINGLE_SUPPLIERS: ActionTypes.TRAINING_EVENTS_DETAIL_BACK,
    },
    'supplier_card_clicked': {
        SINGLE_SUPPLIERS: ActionTypes.SUPPLIER_CARD_CLICKED,
    },
    'landing_was_opened': {
        SINGLE_SUPPLIERS: ActionTypes.LANDING_WAS_OPENED,
    },
    'main_search_was_clicked': {
        SINGLE_SUPPLIERS: ActionTypes.MAIN_SEARCH_WAS_CLICKED,
    },
    'main_search_was_filled': {
        SINGLE_SUPPLIERS: ActionTypes.MAIN_SEARCH_WAS_FILLED,
    },
    'recent_searches_was_clicked': {
        SINGLE_SUPPLIERS: ActionTypes.RECENT_SEARCHES_WAS_CLICKED,
    },
    'search_type_button_was_clicked': {
        SINGLE_SUPPLIERS: ActionTypes.SEARCH_TYPE_BUTTON_WAS_CLICKED,
    },
    'search_result_was_clicked': {
        SINGLE_SUPPLIERS: ActionTypes.SEARCH_RESULT_WAS_CLICKED,
    },
    'show_all_button_was_clicked': {
        SINGLE_SUPPLIERS: ActionTypes.SHOW_ALL_BUTTON_WAS_CLICKED,
    },
    'bottom_all_items_button_was_clicked': {
        SINGLE_SUPPLIERS: ActionTypes.BOTTOM_ALL_ITEMS_BUTTON_WAS_CLICKED,
    },
    'suggestion_close_button_was_clicked': {
        SINGLE_SUPPLIERS: ActionTypes.SUGGESTION_CLOSE_BUTTON_WAS_CLICKED,
    },
    'search_type_dropdown_was_clicked': {
        SINGLE_SUPPLIERS: ActionTypes.SEARCH_TYPE_DROPDOWN_WAS_CLICKED,
    },
}


FEATURE_TYPES = {
    'registration': 'Registration',
    'search': 'Search',
    'saved_suppliers': 'Saved Suppliers',
    'export_to_pdf': 'Export to PDF',
    'user_request': 'User Request',
    'notes': 'Notes',
    'registration_verification': 'Registration Verification',
    'share_by_email': 'Export by email',
    'contact_supplier': 'Contact Supplier',
    'user_verification': 'User Verification', # for device change or by time
    'filtering': 'Filtering',
    'opportunities': 'Opportunities',
    'commodity_codes': 'Commodity Codes',
    'contract_vehicles': 'Contract Vehicles',
    'supplier_profile': 'Supplier Profile',
    'change_view': 'Change View',
    'summary_report': 'Summary Report',
    'events': 'Training Events',
}

PAGES = {
    'about-us': 'About Us',
    'buyers-resources': 'Buyers Resources',
    'codes-detail': 'Separate Commodity Code',
    'contacts': 'Contact Us',
    'contractcodes-tree': 'Contract vehicles',
    'events:detail': 'Event Details',
    'events:list': 'Events',
    'faqs': 'FAQs',
    'getting-started': 'Getting Started',
    'govshop-training': 'Training Videos',
    'home-page': 'Landing',
    'offerings-tree': 'Commodity codes',
    'opportunities': 'Opportunities',
    'opportunity-detail': 'Opportunity Details',
    'profile': 'Profile Settings',
    'public-saved-list-detail': 'Saved List Detail',
    'public-saved-lists': 'Public Saved Lists',
    'saved-list-detail': 'Saved List Detail',
    'saved-lists': 'Saved Lists',
    'search-page': 'Supplier Search',
    'subscription-info': 'Subscription Info',
    'subscription-plans': 'Subscription Plans',
    'supplier-profile': 'Supplier Profile',
    'training-events:detail': 'Training Event Details',
    'training-events:list': 'Training Events',
    'vehicles-detail': 'Separate Contract Vehicle',
}

SUPPLIER_SECTIONS = {
    'general': 'General Info',
    'contact': 'Contact Info',
    'old-contact-info': 'Additional Contacts',
    'certifications': 'Certifications',
    'diversity-statuses': 'Size and Minority Status',
    'featured-products': 'Products and Services',
    'offerings-codes': 'Commodity Codes',
    'past-experience': 'Past Experience',
    'existing-contracts': 'Existing Contracts',
    'external-recognition': 'External Recognition',
    'downloadable-content': 'Downloadable Content',
    'location': 'Locations Served',
    'seo': 'SEO',
}

USER_REQUESTS = {
    REQUEST_TYPES.demo: 'Demo Request',
    REQUEST_TYPES.mailing: 'Mailing List',
    REQUEST_TYPES.contact: 'Contact Us',
    REQUEST_TYPES.profile: 'Supplier Profile',
    REQUEST_TYPES.contract_vehicle: 'Suggest Contract Vehicle',
    REQUEST_TYPES.live_training: 'Live Training Request',
    REQUEST_TYPES.account_support: 'Account Support',
    REQUEST_TYPES.add_your_opportunity: 'Add Your Opportunity',
    REQUEST_TYPES.change_supplier_name: 'Change Supplier Name',
    REQUEST_TYPES.sam_exclusions_form: 'SAM Exclusion Contact',
    REQUEST_TYPES.saved_list: 'Saved List',
    REQUEST_TYPES.consultation: 'Consultation',
}
