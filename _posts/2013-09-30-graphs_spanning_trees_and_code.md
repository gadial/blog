---
id: 2890
title: "על גרפים, עצים פורשים ואיך זה נראה בקוד"
date: 2013-09-30 13:48:47
layout: post
categories: 
  - מבני נתונים ואלגוריתמים
  - תורת הגרפים
  - תכנות
tags: 
  - גרפים
  - מתיאוריה לפרקטיקה
---
<a href="http://www.gadial.net/2013/09/22/kruskal_and_prim_maze_builders/">בפוסט הקודם</a> הצגתי באופן מאוד לא פורמלי ולא מחוייב שני אלגוריתמים לייצור מבוכים - של קרוסקל ושל פרים. המבוכים היו רק תירוץ כדי להציג את האלגוריתמים הללו, שמיועדים לטפל בסיטואציות הרבה יותר כלליות - אלו אלגוריתמים ל<strong>מציאת עץ פורש מינימלי</strong> בגרף.  בפוסט הזה נבין מה זה גרף, מה זה עץ פורש מינימלי ואיך זה רלוונטי לבניית מבוכים. וכדי שלא נהיה באוויר לגמרי, גם נדבר קצת על איך מתכנתים את זה.

<strong>גרף</strong> הוא אחד מהמושגים הבסיסיים במתמטיקה ובמדעי המחשב, ומכיוון שהוא מושג בסיסי הוא גם מאוד פשוט בהגדרתו. גרף כולל שתי קבוצות של אובייקטים: צמתים (שלפעמים נקראים קודקודים) וקשתות. אין ממש מגבלה על מה שצומת יכול להיות - העיקר שכשנדבר על גרף נוכל לדעת בדיוק מי הצמתים שלו; הקשתות לעומת זאת הן תמיד זוגות של צמתים. מבחינה גרפית נוח לחשוב על הצמתים בתור עיגולים, ועל הקשתות בתור קווים שמחברים עיגולים. זה טוב ויפה, אבל בשביל מה לדבר על גרפים? מה הם מייצגים במציאות?

הנה כמה דוגמאות מהשרוול:

<ul>
	<li>הצמתים הם ערים, והקשתות מחברות ערים שיש כביש ישיר ביניהן. בין ערים שאין ביניהן כביש ישיר עדיין יכול להיות <strong>מסלול</strong> שכולל מעבר בכמה ערי ביניים; בעיה מעניינת בתורת הגרפים שנתייחס אליה בהמשך היא מציאה של מסלולים שכאלו.</li>
	<li>הצמתים הם שורות קוד בתוכנית מחשב ויש קשת בין שתי שורות קוד שריצת התוכנית יכולה לעבור מהראשונה שבהן אל השניה. בעיה מעניינת היא לזהות מקומות בתוכנית שפשוט לא ניתן להגיע אליהם ולכן הם מיותרים. היי, זו כמעט אותה בעיה כמו קודם!</li>
<li>הצמתים הם הרצאות שיש להעביר באוניברסיטה, כולל השעות שבהן ההרצאות ניתנות, ויש קשת בין שתי הרצאות שהזמן שלהן חופף ולכן לא יכולות להינתן שתיהן באותו אולם הרצאה. המטרה כאן היא <strong>לצבוע</strong> את הגרף בצבעים כך שכל שני צמתים שמחוברים בקשת צבועים בצבעים שונים; כל צביעה כזו אפשר לתרגם לשיבוץ הרצאות לכיתות על ידי כך שכל צבע ייצג כיתת הרצאה כלשהי (והמטרה היא למצוא צביעה עם מספר נמוך ככל האפשר של צבעים).</li>
</ul>

טוב ויפה, אני מקווה שהבנתם את רוח הדברים. נקודה אחת שכדאי לשים לב אליה היא שהגרף יכול להיות מכוון - ואז לקשתות יש כיוון (מצומת א' לצומת ב') או לא מכוון, ואז כל קשת היא "בין" צמתים א' וב'. אני הולך לדבר אך ורק על גרפים לא מכוונים; בהמשך אפשר יהיה לדבר גם על גרפים מכוונים ולראות מה משתנה (לא הרבה יותר מדי, לרוב, אבל לפעמים יש הבדלים די קריטיים). עוד הנחה חשובה היא שהגרף יהיה <strong>סופי</strong>, דהיינו מספר הצמתים בו הוא סופי. אמנם, עדיין אפשר לעשות דברים גם עבור גרפים אינסופיים אבל הסיפור יותר מסובך עבורם ולא ממש רלוונטי לכל מה שאני הולך לדבר עליו.

עכשיו, איך מייצגים מבוך בעזרת גרף? כפי שנראה יש כמה דרכים שלכל אחת מהן היתרונות שלה. הנה הדרך שנוחה לי עבור <strong>יצירת</strong> מבוך: התאים של המבוך יהיו הצמתים של הגרף, ותהיה קשת בין שני תאים אם ורק אם שני התאים הללו חולקים קיר משותף. כאשר אני מתחיל את אלגוריתם יצירת המבוך, המבוך שלי יהיה "מלא", במובן זה שהוא כולל את כל הקירות האפשריים - כל תא יחובר בקשת לארבעת שכניו (פרט לתאים שנמצאים בקצה המבוך ולכן יש להם פחות שכנים). כעת, מה שאני רוצה לעשות הוא להחליט אילו קירות להסיר על מנת שבמבוך יהיה מסלול יחיד בין כל שני תאים; לשם כך אני צריך לבחור תת-קבוצה של הקשתות, כך שאם מסתכלים רק עליה ומתעלמים מיתר הקשתות (כלומר, מסתכלים על <strong>תת-גרף</strong> של הגרף המקורי) מקבלים גרף שיש בו בדיוק מסלול אחד בין כל שני צמתים. לגרף כזה, שבו יש בדיוק מסלול אחד בין כל שני צמתים, קוראים <strong>עץ</strong>.

הנה הגדרה שקולה של עץ, שבתקווה תהיה ברורה למי שניסו להוכיח את הטענות שזרקתי לאוויר בפוסט הקודם: עץ הוא גרף קשיר וחסר מעגלים. גרף קשיר הוא פשוט גרף שבו יש מסלול בין כל שני צמתים (אבל לא מובטח שהמסלול יחיד) ו"מעגל" בגרף הוא סדרה של צמתים כך שיש קשת בין כל זוג צמתים סמוכים בסדרה ולא חוזרים על אותה הקשת פעמיים (כדי למנוע מצב שבו אנחנו הולכים "קדימה ואז אחורה") והצומת האחרון בסדרה מחובר לצומת הראשון בה. לא קשה להשתכנע שאם גרף קשיר אינו עץ אז הוא כולל מעגל - זה אומר שיש שני צמתים שיש שני מסלולים ביניהם, ולכן אפשר "לחבר" את המסלולים הללו כדי לקבל מעגל; ובדומה, אם יש לנו מעגל בגרף, אז על כל זוג צמתים שעל המעגל יש לנו לפחות שני מסלולים ביניהם ומכאן השקילות.

עכשיו, בהינתן גרף קשיר, תמיד קיים לו לפחות תת-גרף אחד שהוא עץ, ולרוב יש הרבה כאלו. לכל עץ כזה קוראים <strong>עץ פורש</strong> של הגרף. מה שאני בעצם רוצה לעשות הוא למצוא עץ פורש של "גרף המבוך" שיגיד לי אילו קירות להסיר. האינטואיציה לגבי האופן שבו מוכיחים שקיים עץ פורש בגרף קשיר זהה לאינטואיציה שמאחורי בניית המבוך: פשוט מסירים עוד ועוד קשתות ככל שניתן מבלי לפגום בתכונת הקשירות של הגרף, ובסופו של דבר נקבל בהכרח עץ. מדוע? כי לא קשה להוכיח שאפשר להסיר קשת מגרף מבלי לפגום בקשירות שלו אם ורק אם הקשת הזו נמצאת על מעגל כלשהו בגרף. לכן, אם אנחנו מגיעים למצב שבו אין לנו יותר קשתות להסיר, זה סימן שהגרף שלנו הוא חסר מעגלים. הנה אפיון נוסף של עץ: עץ הוא גרף קשיר <strong>מינימלי</strong> ביחס לתכונת הקשירות, דהיינו אם נסיר ממנו קשת כלשהי הוא כבר לא יהיה קשיר (באופן דואלי, עץ הוא גם גרף חסר מעגלים שהוא <strong>מקסימלי</strong> ביחס לתכונה הזו, במובן זה שכל קשת שנוסיף אליו תהפוך אותו לבעל מעגלים - מדוע?). כדאי גם להעיר שאנחנו יודעים בדיוק כמה קשתות הולכות להיות בעץ: כמספר הצמתים פחות 1. אני אשאיר את ההוכחה של הטענה הזו בתור אתגר לקוראים.

אם כן, האלגוריתמים של קרוסקל ופרים הם אלגוריתמים למציאת עצים פורשים של גרפים, אבל הם עושים יותר מזה - הם מוצאים עצים פורשים <strong>מינימליים</strong>. אבל מינימליים ביחס למה? הרי אמרתי לפני שניה שבכל עץ פורש יש אותו מספר קשתות. התשובה היא שקרוסקל ופרים מיועדים לעבוד על גרפים <strong>ממושקלים</strong> - גרפים שבהם לקשתות יש משקל ("מחיר") ואנחנו רוצים למצוא עץ פורש שסכום משקל הקשתות שלו הוא מינימלי, ביחס לכל העצים הפורשים האפשריים של הגרף. בשביל מה זה טוב? ובכן, הנה דוגמה אחת מני רבות: נניח שהצמתים שלנו הם מחשבים, ואנחנו רוצים לחבר את כל המחשבים ברשת. לכל זוג מחשבים שאפשר לחבר יש גם "מחיר" שדורשת התקנת החיבור הזה. ענייני מהירות לא חשובים לנו - כלומר, לא אכפת לנו אם המסלול שמחבר שני מחשבים יהיה ארוך מאוד - כל מה שחשוב לנו הוא שמכל מחשב יהיה מסלול לכל מחשב אחר, ושמחיר ההתקנה של החיבורים יהיה הזול ביותר האפשרי. די בבירור אנחנו זקוקים לעץ, כי הגרף חייב להיות קשיר, וכי מעגל בגרף פירושו שיש לנו קשתות מיותרות ששילמנו עליהן "סתם"; קרוסקל ופרים ימצאו לנו את העץ הזול ביותר מכל העצים האפשריים.

איך זה קשור להגרלה של מבוך? פשוט מאוד: אני אבנה את הגרף של המבוך תוך שאני נותן לכל קשת משקל שהוא מספר אקראי בין 0 ל-1. זה יוביל לכך שהעץ הפורש המינימלי שקרוסקל ופרים ימצאו יהיה מבוך אקראי. אני משתמש כאן במילה "אקראי" בנדיבות - פירושה הוא רק שבהרצות שונות אוכל לקבל שלל מבוכים שונים, שלכל מבוך יש סיכוי להופיע ושהמבוך הממוצע שיופיע "ייראה אקראי", מה שזה לא אומר; אני בפירוש לא מנסה לטעון שהשיטה שלי מגדירה התפלגות אחידה על כל המבוכים האפשריים או כל דבר אחר (אולי היא כן? לא יודע, לא בדקתי, ועם איך שקרוסקל ופרים עובדים, כנראה שממש לא).

לקרוסקל ופרים בגרסתם המלאה נגיע בפוסט הבא. עכשיו אני רוצה שנעבור לדבר על ענייני מימוש, שהם מה שמבדיל את תורת הגרפים של מתמטיקה מתורת הגרפים של מדעי המחשב. ראשית כל, אני לא הולך לכתוב פסאודו-קוד אלא קוד שעובד בפועל, אם כי לא בהכרח בצורה היעילה ביותר שאפשר. בחרתי לעבוד עם Javascript, משלוש סיבות: הראשונה, והעיקרית, היא שבצורה הזו מתאפשר לנו סיפוק מיידי - אני יכול להציג את התוצרים של הקוד (למשל, ייצור מבוך) ישר בתוך הפוסטים עצמם, וכל מי שיש לו דפדפן יכול (בתקווה) להריץ אותם. שנית, זו שפה עם תחביר בסיסי די פשוט שמזכיר את זה של C ו-Java, ולכן יש תקווה שרוב הקוראים שמכירים שפות תכנות יבינו פחות או יותר את הקוד; ולבסוף, זו שפה מספיק מתוחכמת כדי שאוכל לעשות שם דברים רבים בצורה כמעט פסאודו-קודית, להבדיל משפה כמו C שבה חלק מהתעלולים היו דורשים לא מעט "בניית פיגומים" שאני מעדיף לוותר עליה. אני מזהיר מראש שאני לא מתכנן ללמד Javascript, וזו שפה מתעתעת עם כל מני תכונות מוזרות שלא ארחיב יותר מדי עליהן - המטרה היא בסופו של דבר להציג רעיונות באלגוריתמים ומבני נתונים, לא שפת תכנות.

הדבר הראשון שאנחנו רוצים לעשות הוא לייצג גרף כאובייקט בשפת התכנות שלנו. יש אינספור דרכים שונות לעשות את זה. הדרך המתבקשת ביותר היא לייצג גרף בתור זוג של מערכים ("רשימות") - מערך של צמתים, ומערך של קשתות. זו גישה סבירה אבל טיפה בזבזנית מבחינת מקום - למה בעצם צריך לשמור את הצמתים בנפרד? זה הגיוני, אולי, אם יש לצמתים עוד מידע נוסף שמקודד בהם, אבל אני דווקא אעדיף להימנע מכך ככל האפשר. לכן אצלי גרף לא יכיל רשימת צמתים אלא רק מספר, שאסמן ב-{% equation %}n{% endequation %}, שהוא מספר הצמתים שיש בגרף. על הצמתים עצמם אני אחשוב בתור המספרים מ-0 ועד {% equation %}n-1{% endequation %}, כי זה מה שנהוג לעשות במדעי המחשב: אינדקסים של מקומות במערכים מתחילים ברוב שפות התכנות ב-0, ולכן אנחנו רגילים לספור החל מ-0.

קשתות, לעומת זאת, אכן יהיו מיוצגות על ידי מערך של אובייקטים, כאשר כל אובייקט יורכב מזוג מספרים - הצמתים שאליו הם מחוברים - ואולי עוד פרטי מידע, למשל המשקל של הקשת (הרי אמרתי שאנחנו רוצים לעבוד עם גרפים ממושקלים). הנה אם כן הקוד שמגדיר את הפונקציה שמייצרת גרף חדש:

[javascript]
var Graph = function(n){
	this.n = n;
	this.E = new Array();
}
[/javascript]

למי שנראה לו מוזר שאני מגדיר כאן משתנה בזמן שאני בעצם מגדיר פונקציה או משהו - כן, ברוכים הבאים ל-Javascript, זה הדבר הכי מוזר שכנראה תראו פה, אז פשוט תתעלמו. העיקר שאמור לעניין אותנו פה הוא שאני קולט <strong>מראש</strong> את מספר הצמתים בגרף - {% equation %}n{% endequation %} - ואני לא הולך לאפשר לשנות אותו בהמשך כי אין בכך צורך עבור הגרפים שלי. הקשתות, לעומת זאת, מתחילות בתור רשימה ריקה.

עכשיו, האם רשימת קשתות היא באמת רעיון טוב? מצד אחד, זה מקל לעבור סדרתית על כל הקשתות בגרף, ומצד שני, אם אני רוצה לדעת אם יש קשת שמחברת שני צמתים ספציפיים, זה אומר שאני צריך לעבור על כל רשימת הקשתות, וזה ממש בלתי נסלח לפעמים (תחשבו על גרפים עם מיליארד קשתות). כפי שנראה, המימוש שלי הוא לא רע עבור האלגוריתם של קרוסקל אבל לא משהו עבור האלגוריתם של פרים. מימוש חכם יותר מתבסס על רשימה של צמתים, כאשר לכל צומת יש בתוכו רשימה של הקשתות שמחוברות אליו - זה מה שנקרא מימוש ה-Adjacency list של גרף והוא המימוש הסטנדרטי ביותר שלו כשרוצים קצת יעילות. לי זה לא כזה חשוב ואני מעדיף להשאיר את רוב הקוד פשוט, אז ויתרתי על זה.

עכשיו אני הולך להוסיף כמה פונקציות לגרף שאפשר להפעיל אותן, בהינתן גרף, על ידי כתיבת השם שלו, נקודה, ואז את שם הפונקציה, והפונקציה מקבלת את הגרף אוטומטית כפרמטר בשם this. לפונקציות כאלו קוראים <strong>מתודות</strong> של הגרף. בגלל הגישה המוזרה של Javascript לעניינים הללו, כל הפונקציות שאגדיר בהמשך נמצאות בין הסוגרים המסולסלים בקטע הקוד הבא:

[javascript]
Graph.prototype = {
...
}
[/javascript]

(שלוש הנקודות הן לא קוד - הן "כל הפונקציות").

בואו נתחיל עם פונקציה שמוסיפה קשת לגרף. כאן כבר יש לנו "בעיה", כי קשת מוגדרת על ידי זוג הקודקודים שהיא מחוברת אליהם, אבל הגרף לא מכוון, אז הקשת {% equation %}(3,5){% endequation %} היא אותו דבר כמו {% equation %}(5,3){% endequation %}. אז יש בדיקות מפורשות עבור זה ועבור עוד דברים:


[javascript]
add_edge: function(a,b,w){
		if (a &gt;= this.n || b &gt;= this.n){
			return;
		}
		if (a &gt; b){
			this.add_edge(b,a,w);
			return;
		}
		if (this.has_edge(a,b)){
			return;
		}
		var e = [a,b];
		if ('undefined' === typeof w){
			w = Infinity;
		}
		e.w = w;
		this.E.push(e)
		return this;
	},
[/javascript]

הפרמטר w הוא המשקל של הקשת - אם הוא לא ניתן כקלט, נותנים לקשת אוטומטית את המשקל אינסוף (היי, מגניב! ב-Javascript אינסוף הוא כבר חלק מתוך השפה! אפילו ברובי זה לא ככה! רגע, בעצם בגרסה 1.9.2 של רובי כבר יש, נו טוב, רובי מנצחת שוב!)

אתם בטח תוהים מה זה has_edge - ובכן, זו עוד מתודה מתבקשת:

[javascript]
has_edge: function(a,b){
		result = false;
		this.each_edge(function(e){if ((e[0] == a &amp;&amp; e[1] == b) || (e[1] == a &amp;&amp; e[0] == b)) result = true;})
		return result;
	},
[/javascript]

המימוש פה הוא הכי נאיבי שאפשר - עוברים כל כל הקשתות ובודקים האם מצאנו את זו שאנחנו מחפשים. בשביל לעבור על כל הקשתות אני משתמש ב-each_edge שגם היא מתודה שכתבתי שפשוט עוברת קשת-קשת ומפעילה על כל קשת פונקציה שהועברה כפרמטר:
[javascript]
each_edge: function(f){
		for (var i = 0; i &lt; this.E.length; i++){
			f(this.E[i]);
		}
	},
[/javascript]

ואם אני לא רוצה סתם לבדוק אם קשת קיימת אלא ממש למצוא ולהחזיר אותה?

[javascript]
find_edge: function(a,b){
		for (var i = 0; i &lt; this.E.length; i++){
			var e = this.E[i];
			if ((e[0] == a &amp;&amp; e[1] == b) || (e[1] == a &amp;&amp; e[0] == b))
				return e;
		}
		return null;
	},
[/javascript]

בהמשך אצטרך גם להסיר קשתות. האופן שבו מסירים איברים ממערך היא באמצעות הפונקציה splice שיש לה שם קצת מבלבל, אבל עושה כאן את מה שאנחנו מצפים שתעשה:

[javascript]
remove_edge: function(a,b){
		for (var i = 0; i &lt; this.E.length; i++){
			var e = this.E[i];
			if ((e[0] == a &amp;&amp; e[1] == b) || (e[0] == b &amp;&amp; e[1] == a)){
				this.E.splice(i,1);
				return;
			}
		}
	},
[/javascript]

וזהו זה לעת עתה. הקוד הזה בוודאי לא כתוב בצורה אופטימלית ויש כמה שכפולי קוד מעצבנים, אבל זה חלק מהמשחק - נסו לחשוב איך הייתם משפרים אותו.

עכשיו, איך נחבר את זה עם מבוכים? ובכן, בואו ניצור אובייקט חדש של מבוך:

[javascript]
var Maze = {
...
}
[/javascript]

שימו לב שאני יוצר את אובייקט המבוך הזה בצורה שונה מזו שבה יצרתי את האובייקט עבור גרף - הסיבה לכך היא שבקוד הנוכחי שלי אני לא הולך להניח שקיים יותר ממבוך אחד בו זמנית, ולכן מספיק שיהיה לי משתנה אחד שקוראים לו "מבוך", לעומת גרף שרציתי את האפשרות ליצור כמה עותקים שונים ממנו. שוב - אלו לא פרטים טכניים שחשוב להתעמק בהם כאן.

עכשיו לפונקציה שיוצרת מבוך חדש, עם כל הקירות בפנים, ובונה גם את הגרף המתאים:

[javascript]
generate_raw: function(height, width){
		this.G = new Graph(height*width);
		this.height = height;
		this.width = width;
		this.cells = new Array();
		for (var y = 0 ; y &lt; height; y++){
			for (var x = 0; x &lt; width; x++){
				this.cells.push([x,y]);
			}
		}
		for (var y = 0 ; y &lt; height; y++){
			for (var x = 0; x &lt; width; x++){
				if (x &gt; 0){
					this.G.add_edge(this.cell_index([x,y]),this.cell_index([x-1,y]),Math.random());
				}
				if (y &gt; 0){
					this.G.add_edge(this.cell_index([x,y]),this.cell_index([x,y-1]),Math.random());
				}
			}
		}
	},
[/javascript]

אז מה אני עושה כאן? יוצר גרף חדש שמספר הצמתים בו הוא כמספר התאים במבוך. כמו כן אני יוצר בתוך האובייקט של המבוך מערך שמטרתו להכיל את התאים עצמם, ודוחף אליו את כל התאים (תא הוא זוג קואורדינטות - גובה ואורך). כעת יש לי התאמה בין התאים במבוך ובין הצמתים של הגרף - המספר של הצומת בתוך הגרף הוא האינדקס שלו בתוך מערך התאים.

החל משורה 11 אני מוסיף קשתות לגרף: לכל תא במבוך, אם יש תא מעליו אני מוסיף קשת שמתארת את הקיר ביניהם, ואם יש תא משמאלו אני מוסיף קשת שמתארת את הקיר ביניהם. לכל הקשתות אני נותן משקל אקראי בין 0 ל-1 (זה מה ש-Math.random מחזירה).

הורדה של קיר היא דבר קל - פשוט מסירים את הקשת המתאימה. בדומה, אני גם רוצה לאפשר צביעה של קירות בצבעים שונים (זה יהיה מועיל בהמשך) וגם זה מתבצע על ידי שינוי של הקשת המתאימה:
[javascript]
remove_wall: function(a,b){
		this.G.remove_edge(Maze.cell_index(a),Maze.cell_index(b));
	},

	set_wall_color: function(a,b,color){
		e = Maze.G.find_edge(a,b);
		e.color = color;
	},
[/javascript]

ועכשיו בואו נעבור לציור של המבוך. כדי לצייר דברים ב-Javascript נהוג בימינו להשתמש במשהו שנקרא Canvas, שהוא אלמנט שיכול להופיע בתוך ה-HTML של העמוד - זה אחד מהשכלולים של HTML5. אני אניח שכבר יש אובייקט בשם Game שמטרתו לנהל את העניינים ובין היתר כבר העתיק לעצמו את אובייקט ה-Canvas שעליו צריך לצייר את המבוך. הציור ל-Canvas הזה נעשה דרך אובייקט של ה-Canvas שנקרא Context, ואני מניח שגם אותו כבר יש. זה מוביל אותנו למתודה הבאה:

[javascript]
draw: function(){
		Game.context.clearRect(0,0,Game.canvas.width, Game.canvas.height);
		for (var i = 0; i &lt; this.G.E.length; i++){
			var e = this.G.E[i];
			var a = this.cells[e[0]];
			var b = this.cells[e[1]];
			this.draw_wall(a,b, e.color);
		}
		for (var x = 0; x &lt; this.width; x++){
			this.draw_wall([x,0],[x,-1]);
			if (x != this.width-1)
				this.draw_wall([x,this.height-1],[x,this.height]);
		}
		for (var y = 0; y &lt; this.height; y++){
			this.draw_wall([0,y],[-1,y]);
			this.draw_wall([this.width-1,y],[this.width,y]);
		}
	}
[/javascript]

כרגע כל מה שאני עושה הוא למחוק את התוכן הנוכחי של ה-Canvas ולהריץ שלוש לולאות. שתי האחרונות מציירות את הקירות שסביב המבוך, למעט הפינה הימנית-תחתונה שנותרת פרוצה ("כניסה" למבוך); הלולאה הראשונה היא מה שמצייר את הקירות הפנימיים, על פי הקשתות שיש כרגע בגרף. אבל כל עוד לא הראיתי את המימוש של draw_wall בעצם לא עשיתי כלום, אז הנה המימוש שהוא טיפה טכני ולא חייבים להבין את פרטיו:
[javascript]
draw_wall: function(a,b,color){
		if (a == undefined || b == undefined || (Math.abs(a[0]-b[0])+Math.abs(a[1]-b[1])) != 1){
		 return;
		}
		color = color || '#000000';
		Game.context.strokeStyle = color;
		Game.context.fillStyle = color;
		var x = WALL_WIDTH + Math.max(a[0],b[0])*(SQUARE_SIZE + WALL_WIDTH);
		var y = WALL_WIDTH + Math.max(a[1],b[1])*(SQUARE_SIZE + WALL_WIDTH);
		if (a[0] != b[0]){ //vertical wall
			Game.context.fillRect(x-WALL_WIDTH,y-WALL_WIDTH,WALL_WIDTH,SQUARE_SIZE+2*WALL_WIDTH);
		}
		if (a[1] != b[1]) { //horizontal wall
			Game.context.fillRect(x-WALL_WIDTH,y-WALL_WIDTH,SQUARE_SIZE+2*WALL_WIDTH, WALL_WIDTH);
		}
	},
[/javascript]

כאן WALL_WIDTH ו-SQUARE_SIZE הם קבועים שנתתי להם ערכים קודם:

[javascript]
var SQUARE_SIZE = 20;
var WALL_WIDTH = 3;
[/javascript]

לסיום, הנה האובייקט של המשחק שהוא קטן ופשוט יחסית כרגע:
[javascript]
var Game = {
	start: function(){
		Game.canvas = document.getElementById(&quot;canvas&quot;);
		Game.context = canvas.getContext('2d');
		var size = parseInt(document.getElementById(&quot;maze_size&quot;).value);
		Maze.generate_raw(size, size);
		Maze.draw();
	}
}
[/javascript]

והנה ה-HTML שבו הולכים להשתמש בכל זה:
[html]
&lt;input type=&quot;range&quot; min=&quot;2&quot; max=&quot;20&quot; id=&quot;maze_size&quot;&gt;
		&lt;input type=&quot;button&quot; value=&quot;ייצר!&quot; onclick=&quot;Game.start()&quot; /&gt;
		&lt;br /&gt;
		&lt;canvas id=&quot;canvas&quot; width=&quot;600&quot; height=&quot;600&quot;&gt;
		&lt;/canvas&gt;
[/html]

וזהו זה. עכשיו בואו נראה איך זה עובד בפועל אצלנו:

[cf]maze_js[/cf]

<input type="range" min="2" max="20" id="maze_size">
		<input type="button" value="ייצר!" onclick="Game.start()" />
		<br />
		<canvas id="canvas" width="600" height="600">
		</canvas>

לא הכי מרשים, חייבים להודות - כרגע ה"מבוך" הזה כולל את כל הקירות וכל מה שאפשר לשלוט עליו הוא הגודל שלו. בפוסט הבא נסביר מה הרעיון התיאורטי הכללי מאחורי קרוסקל ופרים, ונציג את פרים במלואו, כולל קוד להכל. תתכוננו להופעת אורח מרגשת של מבנה נתונים חדש!