from datetime import datetime
import json
import re
import requests
from typing import Dict, List, Tuple
import settings


def parsing(tuple_: Tuple = None) -> List:
	"""
	Собирает данные об отелях и передает боту
	"""
	locations_search_url = settings.URLS[0]
	querystring = {"query": tuple_[3]}
	locations_search_response = requests.request(
		"GET",
		locations_search_url,
		headers=settings.HEADERS,
		params=querystring
	)
	locations_search_data = json.loads(locations_search_response.text)
	locations_search_result = locations_search(locations_search_data, tuple_)
	if not locations_search_result:
		return []

	list_hotels_url = settings.URLS[1]
	if tuple_[4]:
		querystring = {
			"destinationId": locations_search_result,
			"checkIn": tuple_[8],
			"checkOut": tuple_[9],
			"priceMin": tuple_[4].split(', ')[0],
			"priceMax": tuple_[4].split(', ')[1],
			"sortOrder": 'DISTANCE_FROM_LANDMARK',
		}
	else:
		querystring = {
			"destinationId": locations_search_result,
			"checkIn": tuple_[8],
			"checkOut": tuple_[9]
		}
	list_hotels_response = requests.request(
		"GET",
		list_hotels_url,
		headers=settings.HEADERS,
		params=querystring
	)
	list_hotels_data = json.loads(list_hotels_response.text)
	list_hotels_result = list_hotels(list_hotels_data)
	if not list_hotels_result:
		return list_hotels_result
	else:
		if tuple_[2] == 'lowprice':
			list_hotels_result = list_hotels_result[:int(tuple_[6])]
		elif tuple_[2] == 'highprice':
			list_hotels_result = list_hotels_result[-(int(tuple_[6])):]
		elif tuple_[2] == 'bestdeal':
			list_hotels_result = sort_bestdeal(list_hotels_result, tuple_)
			if len(list_hotels_result) >= int(tuple_[6]):
				list_hotels_result = list_hotels_result[:int(tuple_[6])]

		if not int(tuple_[7]) == 0:
			photos_url = settings.URLS[2]
			photos_list = []
			for i in list_hotels_result:
				querystring = {"id": i.get('id')}
				photos_response = requests.request(
					"GET",
					photos_url,
					headers=settings.HEADERS,
					params=querystring
				)
				photos_data = json.loads(photos_response.text)
				photos_result = get_photos(photos_data)
				photos_result = photos_result[:int(tuple_[7])]
				photos_list.append(photos_result)
			else:
				pass

		if not list_hotels_result:
			return list_hotels_result
		else:
			list_info = [list() for _ in range(len(list_hotels_result))]
			for i in list_hotels_result:
				list_info[list_hotels_result.index(i)].extend(
					[
						i.get("name"),
						i.get("address").get("streetAddress"),
						i.get("landmarks")[0].get("distance"),
						i.get("ratePlan").get("price").get("current"),
					]
				)
				if i.get("ratePlan").get("price").get("fullyBundledPricePerStay", ''):
					ppd = re.search(r'\$\d*\W*\d*', i.get("ratePlan").get("price").get("fullyBundledPricePerStay", '')).group()
					list_info[list_hotels_result.index(i)].append(ppd)
				if not int(tuple_[7]) == 0:
					list_info[list_hotels_result.index(i)].extend(photos_list[list_hotels_result.index(i)])
				else:
					pass
			logging(list_info, tuple_)

			return list_info


def sort_bestdeal(list_: List, tuple_: Tuple):
	"""
	Собирает список отелей для команды bestdeal
	"""
	range_distance = float(tuple_[5])
	list_res = []
	pattern = r'\d*.\d*'
	for i in list_:
		string = i.get("landmarks")[0].get("distance")
		if float(re.search(pattern, string).group()) < range_distance:
			list_res.append(i)
	return list_res


def locations_search(data_: Dict, tuple_: Tuple) -> List:
	"""
	Определяет город, возвращает id города.
	"""
	try:
		if data_['suggestions'][0]['entities'][0]['name'].isupper() == tuple_[3].isupper():
			return data_['suggestions'][0]['entities'][0]['destinationId']
	except Exception:
		return []


def list_hotels(data_: Dict) -> List:
	"""
	Собирает список отелей
	"""
	return data_["data"]["body"]["searchResults"]["results"]


def get_photos(data_: Dict) -> List:
	"""
	Собирает список фото
	"""
	list_photos = []
	for i in data_.get('hotelImages'):
		url = i.get('baseUrl').split('{size}')
		url = 'z'.join(url)
		list_photos.append(url)

	return list_photos


def logging(list_: List, tuple_: Tuple) -> None:
	"""
	Заполняет log файл
	"""
	amount = len(list_)
	with open(tuple_[1], 'a', encoding='utf-8') as log_file:
		log_file.write('\n')
		log_file.write('{}\n'.format(datetime.utcnow()))
		log_file.write('{}\n'.format(tuple_[2]))
		if list_ == []:
			log_file.write('{}\n{}\nЯ не смог ничего найти\n'.format(datetime.utcnow(), tuple_[2]))
		else:
			log_file.write('{}\n{}\nЯ смог найти {} из {} отелей\n'.format(
				datetime.utcnow(), tuple_[2], amount, tuple_[6])
			)
			if '$' in list_[0][4]:
				for i in range(amount):
					log_file.write(
						'Отель - {name}, адрес - {street}, расстояние от центра - {distance}, '
						'цена за ночь - {price}, стоимость за указанные даты - {price_for_all}, {photos}\n'.format(
							name=list_[i][0],
							street=list_[i][1],
							distance=list_[i][2],
							price=list_[i][3],
							price_for_all=list_[i][4],
							photos=', '.join(list_[i][5:])
						))
			else:
				for i in range(amount):
					log_file.write(
						'Отель - {name}, адрес - {street}, расстояние от центра - {distance}, '
						'цена за ночь - {price}, {photos}'.format(
							name=list_[i][0],
							street=list_[i][1],
							distance=list_[i][2],
							price=list_[i][3],
							photos=', '.join(list_[i][4:])
						))


if __name__ == '__main__':

	parsing()
