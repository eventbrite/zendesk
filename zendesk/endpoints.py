"""
API MAPPING

"""

mapping_table = {
    # Rest API: Organizations
    'list_organizations': {
        'path': '/api/v2/organizations.json',
        'method': 'GET',
        'status': 200,
    },
    'show_organization': {
        'path': '/api/v2/organizations/{{organization_id}}.json',
        'method': 'GET',
        'status': 200,
    },
    'create_organization': {
        'path': '/api/v2/organizations.json',
        'method': 'POST',
        'status': 201,
    },
    'update_organization': {
        'path': '/api/v2/organizations/{{organization_id}}.json',
        'method': 'PUT',
        'status': 200,
    },
    'delete_organization': {
        'path': '/api/v2/organizations/{{organization_id}}.json',
        'method': 'DELETE',
        'status': 200,
    },
    # Rest API: Groups
    'list_groups': {
        'path': '/api/v2/groups.json',
        'method': 'GET',
        'status': 200,
    },
    'show_assignable_group': {
        'path': '/api/v2/groups/assignable.json',
        'method': 'GET',
        'status': 200,
    },
    'show_group': {
        'path': '/api/v2/groups/{{group_id}}.json',
        'method': 'GET',
        'status': 200,
    },
    'create_group': {
        'path': '/api/v2/groups.json',
        'method': 'POST',
        'status': 201,
    },
    'update_group': {
        'path': '/api/v2/groups/{{group_id}}.json',
        'method': 'PUT',
        'status': 200,
    },
    'delete_group': {
        'path': '/api/v2/groups/{{group_id}}.json',
        'method': 'DELETE',
        'status': 200,
    },
    # Rest API: Tickets
    'list_tickets': {
        'path': '/api/v2/tickets.json',
        'method': 'GET',
        'status': 200,
    },
    'show_ticket': {
        'path': '/api/v2/tickets/{{ticket_id}}.json',
        'method': 'GET',
        'status': 200,
    },
    'create_ticket': {
        'path': '/api/v2/tickets.json',
        'method': 'POST',
        'status': 201,
    },
    'update_ticket': {
        'path': '/api/v2/tickets/{{ticket_id}}.json',
        'method': 'PUT',
        'status': 200,
    },
    'comment_ticket': {
        'path': '/api/v2/tickets/{{ticket_id}}.json',
        'method': 'PUT',
        'status': 200,
    },
    'delete_ticket': {
        'path': '/api/v2/tickets/{{ticket_id}}.json',
        'method': 'DELETE',
        'status': 200,
    },
    # Rest API: Audits
    'list_audits': {
        'path': '/api/v2/tickets/{{ticket_id}}/audits.json',
        'method': 'GET',
        'status': 200,
    },
    'show_audit': {
        'path': '/api/v2/tickets/{{ticket_id}}/audits/{{audit_id}}.json',
        'method': 'GET',
        'status': 200,
    },
    # Rest API: Attachment
    'create_attachment': {
        'path': '/api/v2/uploads.json',
        'valid_params': ('filename', 'token'),
        'method': 'POST',
        'status': 201,
    },
    # Rest API: Users
    'list_users': {
        'path': '/api/v2/users.json',
        'valid_params': ('page', ),
        'method': 'GET',
        'status': 200,
    },
    'search_users': {
        'path': '/api/v2/users/search.json',
        'valid_params': ('query', 'external_id'),
        'method': 'GET',
        'status': 200,
    },
    'show_user': {
        'path': '/api/v2/users/{{user_id}}.json',
        'method': 'GET',
        'status': 200,
    },
    'create_user': {
        'path': '/api/v2/users.json',
        'method': 'POST',
        'status': 200,
    },
    'update_user': {
        'path': '/api/v2/users/{{user_id}}.json',
        'method': 'PUT',
        'status': 200,
    },
    'delete_user': {
        'path': '/api/v2/users/{{user_id}}.json',
        'method': 'DELETE',
        'status': 200,
    },
    'list_user_identities': {
        'path': '/api/v2/users/{{user_id}}/identities.json',
        'method': 'GET',
        'status': 200,
    },
    'show_identity': {
        'path': '/api/v2/users/{{user_id}}/identities/{{identity_id}}.json',
        'method': 'GET',
        'status': 200,
    },
    'create_identity': {
        'path': '/api/v2/users/{{user_id}}/identities.json',
        'method': 'POST',
        'status': 200,
    },
    'verify_identity': {
        'path': '/users/{user_id}/identities/{{identity_id}}/verify',
        'method': 'PUT',
        'status': 200,
    },
    'make_identity_primary': {
        'path': '/api/v2/users/{{user_id}}/user_identities/{{identity_id}}/make_primary',
        'method': 'POST',
        'status': 200,
    },
    'delete_identity': {
        'path': '/api/v2/users/{{user_id}}/user_identities/{{identity_id}}',
        'method': 'DELETE',
        'status': 200,
    },
    # Rest API: Tags
    'list_tags': {
        'path': '/api/v2/tags.json',
        'method': 'GET',
        'status': 200,
    },
    # Rest API: Ticket Fields
    'list_ticket_fields': {
        'path': '/api/v2/ticket_fields.json',
        'method': 'GET',
        'status': 200,
    },
    # Rest API: Macros
    'list_macros': {
        'path': '/api/v2/macros/active.json',
        'method': 'GET',
        'status': 200,
    },
    # Rest API: Search
    'search': {
        'path': '/api/v2/search.json',
        'valid_params': ('query'),
        'method': 'GET',
        'status': 200,
    },
    # Rest API: Categories
    'show_category': {
        'path': '/api/v2/categories/{{category_id}}.json',
        'method': 'GET',
        'status': 200
    },
    'list_categories': {
        'path': '/api/v2/categories.json',
        'method': 'GET',
        'status': 200
    },
    'list_category_forums': {
        'path': '/api/v2/categories/{{category_id}}/forums.json',
        'method': 'GET',
        'status': 200
    },
    'create_category': {
        'path': '/api/v2/categories.json',
        'method': 'POST',
        'status': 201
    },
    'update_category': {
        'path': '/api/v2/categories/{{category_id}}.json',
        'method': 'PUT',
        'status': 200
    },
    'delete_category': {
        'path': '/api/v2/categories/{{category_id}}.json',
        'method': 'DELETE',
        'status': 200
    },
    # Rest API: Forums
    'show_forum': {
        'path': '/api/v2/forums/{{forum_id}}.json',
        'method': 'GET',
        'status': 200
    },
    'list_forums': {
        'path': '/api/v2/forums.json',
        'method': 'GET',
        'status': 200
    },
    'create_forum': {
        'path': '/api/v2/forums.json',
        'method': 'POST',
        'status': 201
    },
    'update_forum': {
        'path': '/api/v2/forums/{{forum_id}}.json',
        'method': 'PUT',
        'status': 200
    },
    'delete_forum': {
        'path': '/api/v2/forums/{{forum_id}}.json',
        'method': 'DELETE',
        'status': 200
    },
    # Rest API: Forum Entries (topics)
    'show_topic': {
        'path': '/api/v2/topics/{{topic_id}}.json',
        'method': 'GET',
        'status': 200
    },
    'show_multiple_topics': {
        'path': '/api/v2/topics/show_many.json',
        'valid_params': ('ids'),
        'method': 'GET',
        'status': 200
    },
    'list_topics': {
        'path': '/api/v2/forums/{{forum_id}}/topics.json',
        'method': 'GET',
        'status': 200
    },
    'create_topic': {
        'path': '/api/v2/topics.json',
        'method': 'POST',
        'status': 201
    },
    'update_topic': {
        'path': '/api/v2/topics/{{topic_id}}.json',
        'method': 'PUT',
        'status': 200
    },
    'delete_topic': {
        'path': '/api/v2/topics/{{topic_id}}.json',
        'method': 'DELETE',
        'status': 200
    },
    # Rest API: Topic Comments
    'list_comments': {
        'path': '/api/v2/topics/{{topic_id}}/comments.json',
        'method': 'GET',
        'status': 200
    },
    'show_comment': {
        'path': '/api/v2/topics/{{topic_id}}/comments/{{comment_id}}.json',
        'method': 'GET',
        'status': 200
    },
    'create_comment': {
        'path': '/api/v2/topics/{{topic_id}}/comments.json',
        'method': 'POST',
        'status': 201
    },
    'update_comment': {
        'path': '/api/v2/topics/{{topic_id}}/comments/{{comment_id}}.json',
        'method': 'PUT',
        'status': 200
    },
    'delete_comment': {
        'path': '/api/v2/topics/{{topic_id}}/comments/{{comment_id}}.json',
        'method': 'DELETE',
        'status': 200
    },
}
