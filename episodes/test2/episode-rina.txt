init -1 python:

    build.archive("rina", "all")
    build.classify('game/' + ramu.fn_getdir() + '/**', 'rina')
    
    rast.register('rina_qna',
        title='Rina qna',
        start='rina_qna', 
        synopsis='Question and answer with Rina',
        tags='demo,npc'
    )

    rina = npc(
        id='rina',
        name='Rina',
        callname='Rin',
        lastname='Liah'
    )
    
    rina.set_phonenum()
    rina.by_expression('0',(223,181))    
   
label rina_qna:

    show demo red
    show rina at npc_align(0.8,1)
    with dissolve
    mc 'Uh, Hi!'
    rina @0_happy "I'm happy to meet you..."
    rina "You came by selecting episode?"
    mc "Yes. I was."
    rina @0_blush "Great!"
    rina "It's a first step to understand what is Episodes in Ramen"
    rina "Episodes can be a side-stories to a your main visual novel.{w} Where every story can have it's own start and ending."
    rina "Episodes can be a book-titles in your visual novel library."
    rina "And offcouse it's can be a episodes inside your story."
    mc "Modular?"
    rina "Yes, within options"
    label .end:

        rina "As a simple demo, this episodes end here."
        mc "What if..."
        hide rina
        with dissolve
        mc "Great! She is gone."
        return

label rina_phonedemo:

    rina "[mc_name]?! Hello?"
    mc "Yeah?"
    rina "I'm calling your from demo_floor4_d1"
    mc "What do you meant?"
    rina "Take your time, and see the source code."
    mc "Fine, I will do that."
    rina "See you."

    return

label demo_floor4_d1:
    
    show demo red
    "Rina call you..."
    $ rina.phonein('label','phonedemo')
    "rbc.answered=[rbc.answered]\nTrue if the call is answered"
    jump ramen_scene_map

label demo_floor3_d2:
    show demo blue
    "You decide to call Rina."
    $ rina.phoneout('json','chat')
    "You could also chose whom to call using the phone interface."
    "if label not exist, or json file not exist, the call will be ignored."
    jump ramen_scene_map
    
label demo_floor3_d1:
    show demo red
    show rina
    rina "[mc_name]!"
    rina @0_blush "For your information, this label and me was inside 'episode-rina'"
    mc "Acknowledge!"
    rina "If 'episode rina' removed; You will end up with a 'Nothing responding...'"
    rina "and error if you select any of 'Phone' demo."
    mc "Yes. Mam!"
    rina @0_happy "Hahaha!"
    jump ramen_scene_map
    