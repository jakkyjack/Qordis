import discord
from discord.ext import commands
from market import buy_parse, get_icon, beautify_input
from relics import relic_parse
token = 'NDc4MDQ1NTIyMDM3NTcxNjE0.Dl5yBw.5wzPsJSCSrS2wEgtX85Mj8HxgJ4'
client = commands.Bot(command_prefix = '/')
server = discord.Member


@client.event
async def on_ready():
    print('Ready for operation, Operator')
    print('Establishing Link as...')



# @client.event
# async def on_message(message):
#     try:
#         await client.process_commands(message)
#     except:
#         await client.send_message(message.channel, 'No listings found, Operator. Please check spe -LLINGGG YOU IDIOT - ')

# @client.event
# async def on_command(price):
#     await client.say('No listings found, Operator. Please check spe -LLINGGG YOU IDIOT - ')


@client.command(pass_context = True)
async def buy(ctx, *args):
    await client.send_typing(ctx.message.channel)
    await client.add_reaction(ctx.message, '\u2705')
    user_input = beautify_input(args)
    offers = buy_parse(user_input)
    user = []
    plat = []
    embed_body = ''
    x = 1
    for i in offers:
        user.append(i[0])
        plat.append(str(i[1]))
        embed_body += "{0: <50}{2:^50}{1: >50}\n".format(str(i[1])+'p',i[0],'|')
        x += 1

    if len(offers) != 0:
        embed = discord.Embed(color=0x6bb0f4)#title="Top 5 Listings for: " + ' '.join(args).title(),url='https://warframe.market/items/'+'_'.join(args).lower(), color=0x6bb0f4)
        embed.set_author(name="Top 5 Listings for: " + ' '.join(user_input).title(),url='https://warframe.market/items/'+'_'.join(user_input).lower(), icon_url='https://warframe.market/static/assets/icons/en/Cephalon_Suda_Augment_Mod.3fb65da0df06f5bd39adccc383a44aa2.png')
        embed.add_field(name='Plat - User', value=embed_body,inline=False)
        embed.add_field(name='\a', value='Use 1⃣-5⃣ to choose an order.', inline=False)
        embed.set_thumbnail(url=get_icon(user_input))
        #embed.set_footer(text='Qordis Bot Powered by Python',icon_url='https://warframe.market/static/assets/icons/en/Cephalon_Suda_Augment_Mod.3fb65da0df06f5bd39adccc383a44aa2.png')
        bot_answer = await client.send_message(ctx.message.channel, embed=embed)
        await client.delete_message(ctx.message)

        emoji_list = ['1⃣','2⃣','3⃣','4⃣','5⃣']

        for emoji in (emoji_list):
            await client.add_reaction(bot_answer, emoji)

        while 1==1 :
            wait_for_order = await client.wait_for_reaction(user=ctx.message.author, message=bot_answer, emoji=emoji_list)
            order_reaction = wait_for_order[0].emoji
            await client.remove_reaction(bot_answer, order_reaction, ctx.message.author)
            order_reaction = int(order_reaction.strip('⃣')) - 1
            whisper_string = '/w ' + user[order_reaction] + ' Hi! I want to buy: ' + ' ' .join(user_input).title() + ' for ' + plat[order_reaction] + ' platinum. (warframe.market)'
            print(whisper_string)

            embed.set_field_at(1, name='\a', value=whisper_string, inline=False)
            await client.edit_message(bot_answer,embed=embed)
    else:
        await client.say('No listings found, Operator. Please check spelling')


@client.command(pass_context = True)
async def p(ctx, *args):
    await client.send_typing(ctx.message.channel)
    await client.add_reaction(ctx.message, '\u2705')
    user_input = beautify_input(args)
    offers = buy_parse(user_input)
    user = []
    plat = []
    embed_body = ''
    x = 1
    for i in offers:
        user.append(i[0])
        plat.append(str(i[1]))
        embed_body += "{0: <50}{2:^50}{1: >50}\n".format(str(i[1])+'p',i[0],'|')
        x += 1
    plat = [int(i) for i in plat]
    if len(offers) != 0:
        embed = discord.Embed(color=0x6bb0f4)
        embed.set_author(name="Average Price for: " + ' '.join(user_input).title(),url='https://warframe.market/items/'+'_'.join(user_input).lower(), icon_url='https://warframe.market/static/assets/icons/en/Cephalon_Suda_Augment_Mod.3fb65da0df06f5bd39adccc383a44aa2.png')
        embed.add_field(name=str(int(sum(plat)/len(plat)))+' Platinum', value='Click \u2139 for Item Listings...',inline=False)
        embed.set_thumbnail(url=get_icon(user_input))
        #embed.set_footer(text='Qordis Bot Powered by Python',icon_url='https://warframe.market/static/assets/icons/en/Cephalon_Suda_Augment_Mod.3fb65da0df06f5bd39adccc383a44aa2.png')
        bot_answer = await client.send_message(ctx.message.channel, embed=embed)
        await client.delete_message(ctx.message)

        info_emoji = '\u2139'
        emoji_list = ['1⃣', '2⃣', '3⃣', '4⃣', '5⃣']


        await client.add_reaction(bot_answer, info_emoji)

        while 1==1 :
            wait_for_order = await client.wait_for_reaction(user=ctx.message.author, message=bot_answer, emoji=info_emoji)
            order_reaction = wait_for_order[0].emoji
            await client.remove_reaction(bot_answer, order_reaction, ctx.message.author)
            await client.remove_reaction(bot_answer, order_reaction, ctx.message.server.me)
            embed.set_field_at(0,name='Plat - User', value=embed_body, inline=False)
            embed.add_field(name='\a', value='Use 1⃣-5⃣ to choose an order.', inline=False)
            await client.edit_message(bot_answer, embed=embed)

            for emoji in (emoji_list):
                await client.add_reaction(bot_answer, emoji)

            while 1==1 :
                wait_for_order = await client.wait_for_reaction(user=ctx.message.author, message=bot_answer,
                                                                emoji=emoji_list)
                order_reaction = wait_for_order[0].emoji
                await client.remove_reaction(bot_answer, order_reaction, ctx.message.author)
                order_reaction = int(order_reaction.strip('⃣')) - 1
                whisper_string = '/w ' + user[order_reaction] + ' Hi! I want to buy: ' + ' '.join(
                    user_input).title() + ' for ' + str(plat[order_reaction]) + ' platinum. (warframe.market)'
                print(whisper_string)

                embed.set_field_at(1, name='\a', value=whisper_string, inline=False)
                await client.edit_message(bot_answer, embed=embed)
                # wait_for_order = await client.wait_for_reaction(user=ctx.message.author, message=bot_answer, emoji=emoji_list)
                # order_reaction=wait_for_order[0].emoji
                #
                # for emoji in (emoji_list):
                #     await client.add_reaction(bot_answer, emoji)
                #
                #
                # await client.remove_reaction(bot_answer, order_reaction, ctx.message.author)
                #
                # order_reaction = int(order_reaction.strip('⃣')) - 1
                # whisper_string = '/w ' + user[order_reaction] + ' Hi! I want to buy: ' + ' '.join(user_input).title() + ' for ' + plat[order_reaction] + ' platinum. (warframe.market)'
                # embed.set_field_at(1, name='\a', value=whisper_string, inline=False)

    else:
        await client.say('No listings found, Operator. Please check spelling')

@client.command(pass_context = True)
async def relic(ctx, *args):
    await client.send_typing(ctx.message.channel)
    await client.add_reaction(ctx.message, '\u2705')

    pretty_input = beautify_input(args)
    print(pretty_input)

    try:
        embed = discord.Embed(color=0x6bb0f4)
        embed.set_author(name="Relic Drop Table: ", icon_url='https://warframe.market/static/assets/icons/en/Cephalon_Suda_Augment_Mod.3fb65da0df06f5bd39adccc383a44aa2.png')
        embed.add_field(name=' '.join(((pretty_input[0], pretty_input[1]))).title(), value=relic_parse((pretty_input[0],pretty_input[1])), inline=True)

        if len(pretty_input) == 3:
            print('2 relics')
            embed.add_field(name=' '.join(((pretty_input[0], pretty_input[2]))).title(), value=relic_parse((pretty_input[0], pretty_input[2])), inline=True)

        elif len(pretty_input) == 4:
            print('3 relics')
            embed.add_field(name=' '.join(((pretty_input[0], pretty_input[2]))).title(), value=relic_parse((pretty_input[0], pretty_input[2])), inline=True)

            embed.add_field(name=' '.join(((pretty_input[0], pretty_input[3]))).title(), value=relic_parse((pretty_input[0], pretty_input[3])), inline=True)

        elif len(pretty_input) == 5:
            print ('4 Relics')
            embed.add_field(name=' '.join(((pretty_input[0], pretty_input[2]))).title(), value=relic_parse((pretty_input[0], pretty_input[2])), inline=True)

            embed.add_field(name=' '.join(((pretty_input[0], pretty_input[3]))).title(), value=relic_parse((pretty_input[0], pretty_input[3])), inline=True)

            embed.add_field(name=' '.join(((pretty_input[0], pretty_input[4]))).title(), value=relic_parse((pretty_input[0], pretty_input[4])), inline=True)

        else:
            await client.say('No Relics found, Operator. Please check spelling')

            pass

        await client.send_message(ctx.message.channel, embed=embed)
        await client.delete_message(ctx.message)
    except:
        await client.say('No Relics found, Operator. Please check spelling')
        pass


client.run(token)