---
title: "בעקבות השערת הרצף, חלק א': מבוא"
layout: post
categories:
  - תורת הקבוצות
tags:
  - השערת הרצף
image: "main/forcing.png"
---


<h2>מה זו השערת הרצף?</h2>

ל<a href="https://gadial.net/2019/10/19/what_is_set_theory/">סדרת הפוסטים</a> על תורת הקבוצות שהתחלתי לכתוב פה לפני כמה שנים וחזרתי אליה עכשיו הייתה תמיד מטרה נסתרת אחת - להגיע בסופו של דבר אל ההוכחה של אי התלות ב-ZFC של <strong>השערת הרצף</strong>. ההוכחה הזו היא במובן מסויים שלב המעבר מתורת הקבוצות ה"נאיבית", זו שנלמדת בקורס ראשון בנושא באוניברסיטה, אל עבר תורת הקבוצות ה"אקסיומטית", המורכבת יותר. בפוסטים האחרונים השלמנו את הידע הרלוונטי החסר והגענו לשלב שבו אפשר לנסח את ההשערה; בפוסט הזה אני רוצה לחזור על הניסוח, להסביר אותו קצת יותר לעומק ובפרט לתאר מה יהיו הקווים הכלליים של ההוכחה שאציג בפוסטים הבאים.

הנה הניסוח הכי פשוט להשערת הרצף שדורש כמעט אפס ידע קודם: השערת הרצף אומרת שלא קיימת קבוצה {% equation %}\mathbb{N}\subseteq A\subseteq\mathbb{R}{% endequation %} כך ש-{% equation %}\left|\mathbb{N}\right|<\left|A\right|<\left|\mathbb{R}\right|{% endequation %}, כשהסימון {% equation %}\left|A\right|<\left|B\right|{% endequation %} לשתי קבוצות כלשהן {% equation %}A,B{% endequation %} אומר שקיימת פונקציה חד-חד-ערכית {% equation %}f:A\to B{% endequation %} אבל לא קיימת פונקציה כזו שהיא גם חד-חד-ערכית וגם על. במילים אחרות, השערת הרצף אומרת שאין "עוצמת ביניים" בין העוצמה של {% equation %}\mathbb{N}{% endequation %} והעוצמה של {% equation %}\mathbb{R}{% endequation %}. ראינו בפוסטים הקודמים שנהוג לסמן {% equation %}\left|\mathbb{N}\right|=\aleph_{0}{% endequation %} ואפשר להוכיח ש-{% equation %}\left|\mathbb{R}\right|=2^{\aleph_{0}}{% endequation %}, אז השאלה היא האם עבור {% equation %}\aleph_{1}{% endequation %}, העוצמה "הבאה בתור" אחרי {% equation %}\aleph_{0}{% endequation %}, מתקיים {% equation %}\aleph_{1}=2^{\aleph_{0}}{% endequation %}. זו השערת הרצף.

הניסוח קל, אבל התשובה לשאלה האם ההשערה נכונה או לא? קשה. 

<h2>על מערכות של אקסיומות ואיך דברים יכולים להיות בלתי תלויים בהן</h2>

בשנת 1900 דויד הילברט נשא נאום שבו הציג 23 בעיות מתמטיות שלדעתו היה כדאי לעולם המתמטי לעסוק בהן. השערת הרצף הייתה הבעיה הראשונה; מכאן אפשר לראות גם מה הייתה חשיבות תורת הקבוצות למתמטיקה באותו הזמן. תורת הקבוצות הייתה הבסיס שמעליו נבנתה יתר המתמטיקה, ולכן השערת הרצף נתפסה בתור שאלה יסודית, מהותית, על הבסיס של המתמטיקה.

בשנת 1905 ברטרנד ראסל פרסם את מה שנקרא "הפרדוקס של ראסל" ופוצץ את תורת הקבוצות לחתיכות. הפרדוקס, כזכור, מגדיר את קבוצת "כל הקבוצות שאינן איבר של עצמן". הקבוצה הזו לא יכולה להיות איבר של עצמה כי זה מוביל לסתירה, אבל גם לא יכולה שלא להיות איבר של עצמה, כי גם זה מוביל לסתירה; המסקנה היא שאין קבוצה כזו, אבל הגישה הנאיבית לתורת הקבוצות בהחלט איפשרה לבנות קבוצה כזו. בצורה הזו המתמטיקאים למדו בצורה כואבת שאי אפשר לנפנף ידיים ולקוות שיהיה בסדר - כשבאים לבנות משהו שעליו רוצים לבסס את כל המתמטיקה, צריך לעשות את זה בצורה זהירה, עם מערכת אקסיומות שתהיה חזקה אבל לא חזקה מדי. נולדו כל מני גישות ל"איך לעשות את זה" אבל הגישה האחת שהפכה להיות הסטנדרט במתמטיקה הייתה זו של מערכת האקסיומות ZFC; מערכת האקסיומות של צרמלו-פרנקל יחד עם אקסיומת הבחירה. 

ב-ZFC יש אקסיומות כדוגמת "אם לשתי קבוצות יש אותן איברים הן שוות זו לזו" ו"בהינתן קבוצה של קבוצות, קיימת קבוצה שהיא האיחוד של כולן" ו"קיימת קבוצה אינסופית" (בניסוחים יותר פורמליים). כלומר, הן נותנות לנו מושג כלשהו לגבי מה זו קבוצה ואילו קבוצות קיימות ואילו קבוצות אפשר לבנות, אבל מה שקריטי להבין זה שהן <strong>לא תופסות הכל</strong>. בהחלט ייתכן שיהיו תכונות של "יקום הקבוצות" שלא ניתן להוכיח באמצעותן, עוד לפני שאנחנו מדברים ספציפית על השערת הרצף. כי בסופו של דבר, מה זו הוכחה? הוכחה היא סדרה של טענות שכל אחת נובעת מקודמות לה או שהיא אקסיומה; זה סוג של אובייקט מתמטי <strong>די פשוט</strong>. אין איזו התחייבות קסומה שתבטיח לנו שכל תכונה של יקום הקבוצות, מורכבת ככל שתהיה, תוכל להיתפס על ידי האובייקט המתמטי הפשוט הזה. אז זה שיש דברים שאי אפשר להוכיח או להפריך - זה בפני עצמו לא כזה מפתיע (קצת יותר מפתיע, אולי, היא ההבנה שלא משנה מה נעשה, לא נוכל למצוא מערכת אקסיומות "מספיק טובה", אבל זה כבר דיון נפרד, על משפטי אי-השלמות של קורט גדל).

דבר אחד שקריטי להבין על מערכות של אקסיומות הוא שאפילו אם אנחנו מדברים עליהן כשיש לנו בראש יקום קונקרטי כלשהו ("יקום כל הקבוצות"), בפועל בהחלט אפשרי שיהיו <strong>עוד</strong> "יקומים אלטרנטיביים" שבהם האקסיומות נכונות. בפרט, יכולים להיות "יקומי צעצוע" קטנים שעדיין מקיימים את כל האקסיומות למרות שהם בבירור לא מה שאנחנו מתכוונים אליו.

הפאנץ' עכשיו הוא זה: אם טענה כלשהי ניתנת להוכחה מתוך מערכת אקסיומות, זה אומר שהיא נכונה <strong>בכל</strong> יקום שמקיים את האקסיומות. לא משנה כמה הוא קטן או מוזר. ולכן בפרט אם יש לנו שני "יקומי צעצוע" שמתאימים ל-ZFC, כך שבאחד מהם השערת הרצף נכונה ובשני השערת הרצף אינה נכונה, זה מוכיח שהשערת הרצף לא ניתנת להוכחה מתוך האקסיומות, וגם לא ניתנת להפרכה כי "הפרכה" היא בסך הכל הוכחה של הטענה ההפוכה ("השערת הרצף אינה נכונה").

זה בדיוק, אבל בדיוק, מה שאנחנו הולכים לעשות. לבנות שני "יקומי צעצוע" כאלו, מבלי שאף אחד מהם יהיה <strong>ה</strong>יקום, בה' הידיעה, של תורת הקבוצות.

<h2>לא הבנו כלום, נא לתת דוגמא</h2>

אוקיי, בואו נניח שזה היה מאוד לא ברור ואנחנו רוצים לקבע את זה בדוגמא קצת יותר מוכרת, האם יש כזו? כן. <a href="https://gadial.net/2009/04/26/continuum_hypothesis_light/">יש לי פוסט על זה</a>, אבל בואו נחזור על זה ונשתמש בדוגמא הקלאסית ביותר לסיטואציה הזו: גאומטריה. בגאומטריה האוקלידית יש כל מני הגדרות ועקרונות יסוד ובנוסף לכך חמש אקסיומות: ארבע מהן פשוטות יחסית (בין כל שתי נקודות אפשר למתוח קו אחד ויחיד; כל קו אפשר להמשיך לישר עד אין קץ; בהינתן שתי נקודות אפשר לצייר מעגל שמרכזו באחת מהן ועובר דרך האחרת; כל הזוויות הישרות חופפות זו לזו) ואקסיומה חמישית, מסובכת, "אקסיומת המקבילים" (בהינתן ישר ונקודה מחוץ לישר, אפשר להעביר מקביל אחד ויחיד לישר דרך הנקודה; הניסוח המקורי מסובך עוד יותר).

הגאומטריה האוקלידית באה לתאר את מה שאנחנו מכירים בבית הספר בתור גאומטריה של המישור, וקל לנו לדמיין בתור איזה דף נייר אינסופי לכל הכיוונים שאנחנו מציירים עליו קווים ונקודות ומעגלים. דף הנייר האינסופי הזה הוא מה שאנחנו מכנים <strong>מודל</strong> של אקסיומות הגאומטריה האוקלידית: זה אובייקט כלשהו שהאקסימות מתקיימות עבורו; מעין "יקום מתמטי" שעונה ל"חוקי הטבע" שהאקסיומות מתארות. אבל קיומו של יקום מתמטי אחד לא שולל את קיומם של יקומים מתמטיים אחרים.

הנה יקום אחר לדוגמא: כדור. מכירים כדורים? בוודאי, אנחנו חייבים על אחד כזה (או משהו שדומה מספיק לכדור). פני כדור הם בוודאי יקום מתמטי נחמד, ואם אנחנו מתרכזים רק בחתיכה קטנה מהכדור, היא אפילו נראית באופן מקומי כמו נייר שטוח אוקלידי, אבל הכדור הזה <strong>ממש לא </strong>מקיים את האקסיומות של אוקלידס. האופן שבו "ישר" מתפרש במודל של הכדור הוא בתור מה שנקרא בגאומטריה <strong>מעגל גדול</strong>, שזה מעגל שמצוייר על פני הכדור שאם חותכים את הכדור על פיו, מקבלים שני חצאי כדור זהים. למשל, בכדור הארץ קו המשווה הוא דוגמא למעגל גדול כזה. אם ניקח את הקוטב הצפוני והדרומי, יש <strong>הרבה</strong> מעגלים גדולים שעוברים דרך שניהם, וזה מפר את האקסיומה הראשונה של אוקלידס; וגם האקסיומה השניה מופרת כי אם אנחנו ממשיכים קו שנמצא על מעגל גדול, מתישהו הוא יחזור אל נקודת ההתחלה שלו במקום להמשיך עד אין קץ. בקיצור, הגאומטריה הכדורית לא משחקת יפה <strong>בכלל</strong> עם האקסיומות של אוקלידס. זה יקום מתמטי אחר, מעניין בזכות עצמו, שלא קשור אליהן.

אבל בנוסף לגאומטריה הכדורית יש עוד סוג של גאומטריה, <strong>גאומטריה היפרבולית</strong>, שכן משחקת יפה עם האקסיומות של אוקלידס - כל ארבע האקסיומות הראשונות נכונות בה, ורק האקסיומה החמישית לא נכונה (כי אפשר להעביר <strong>הרבה</strong> מקבילים ולא רק אחד). איך נראה היקום הזה? יש לו שלל תיאורים שונים אבל אחד מהפופולריים והנוחים שבהם הוא זה שבו היקום נראה כמו אוכף (או חטיף פרינגלס). אני לא אכנס לפרטים כי זה לא פוסט על גאומטריה היפרבולית.

אם כן, הסיטואציה היא כזו: יש לנו יקום מתמטי אחד שבו כל חמש האקסיומות של אוקלידס נכונות ("דף נייר אינסופי") ויש לנו יקום מתמטי אחר שבו ארבעת הראשונות נכונות אבל החמישית לא נכונה ("חטיף פרינגלס") וכעת נשאלת השאלה מהו היקום המתמטי ה"נכון". התשובה היא ששניהם נכונים - שניהם זה משהו שקיים במציאות. אפשר לחדד את הטיעון הזה עוד יותר אם עוברים לדבר גם על שלושה ממדים: אם קיים יקום מתמטי שבו הגאומטריה האוקלידית התלת ממדית נכונה, אז אפשר לקחת את היקום הזה ו<strong>לבנות בתוכו</strong> את האוכף של הגאומטריה ההיפרבולית: במילים אחרות, הטיעון הוא "אם היקום של הגאומטריה האוקלידית קיים, אז גם היקום של הגאומטריה ההיפרבולית קיים" (וגם ההפך עובד).

יש הבדל עקרוני אחד בין הסיפור של אקסיומת המקבילים והשערת הרצף. במקרה של אקסיומת המקבילים, שני היקומים המתמטיים שלנו הם לא "יקומי צעצוע". הם שני יקומים אלטרנטיביים ששניהם נראים כמו מודל "תקין" של ארבע האקסיומות הראשונות של אוקלידס. זה אומר שגם אחרי שנסיים את ההוכחה שהשערת הרצף לא תלויה ב-ZFC עדיין תישאר בחלל האוויר השאלה הכבדה יותר: אז מה קורה ביקום "האמיתי" של תורת הקבוצות? האם שם השערת הרצף נכונה או לא? האם בכלל אפשר לדבר על יקום אמיתי אחד ספציפי של תורת הקבוצות? אולי יש כמה יקומים לגיטימיים שונים, שבאחד מהם השערת הרצף נכונה ובאחר לא?

המתמטיקאים והפילוסופים של המתמטיקה בהחלט מנסים לענות לשאלות הללו, אבל אני מבין בזה מספיק בדיוק כדי שאוכל לומר שאני לא מבין בזה <strong>כלום</strong> ולכן אפילו לא אנסה. מבחינתי הסיפור יסתיים אחרי שאסיים את ההוכחה שהשערת הרצף לא תלויה ב-ZFC, למרות שכמובן - האקשן האמיתי של תורת הקבוצות האקסיומטית רק מתחיל בשלב זה.

<h2>אוקיי אבל מה עושים ברמה הטכנית?</h2>

אני אקדיש את הפוסטים הבאים להסבר טכני שייכנס ככל שניתן לפרטים הקטנים. זה לא נושא שאני מכיר טוב בעצמי, ורוב הנסיונות שלי בעבר ללמוד אותו הסתיימו בכך שדילגתי על פרטים טכניים שהרגשתי לא נוח מכך שאני מדלג עליהם; סדרת הפוסטים הזו תהיה בין היתר נסיון שלי עצמי להשתכנע שאני מבין את הנושא מספיק טוב (אבל אין לי מספיק ידע "מסביב" כדי להעשיר את ההצגה שלו). אני אלך בצורה די צמודה על פי הגישה וההגדרות שבספר Forcing for Mathematicians של Weaver, שהוא לטעמי ספר מצוין שניגש ישר ולעניין לנושא אבל מצליח להיות ברור מאוד; ספרים אחרים (למשל Set Theory של Jech או Set Theory של Kunen) נוקטים בהגדרות טיפה שונות, אבל לא משהו מהותי.

הדבר הראשון שצריך לעשות באופן מסודר הוא להציג באופן מלא את ZFC, איך בדיוק מערכת האקסיומות הזו מוגדרת ומה היא כוללת, ומה זה אומר שמשהו מקיים אותה. כאן אנחנו קצת גולשים אל לוגיקה מתמטית, אבל לא בצורה דרסטית יותר מדי. אמנם, הצגתי את ZFC כבר במסגרת הפוסטים הקודמים, אבל לא היה פוסט שבו הצגתי אותה בצורה מלאה מההתחלה עד הסוף, אז נתחיל מזה.

אחר כך מגיעה התוצאה המעניינת באמת הראשונה בהקשר שלנו - הוכחה שאפשר להניח שיש מעין "יקום זעיר" {% equation %}\mathcal{M}{% endequation %} (כמה זעיר? הוא יהיה קבוצה בת מניה, למרות שבמבט ראשון זה נראה אבסורדי לגמרי) שמקיים במובן מסוים את ZFC ואפשר להתייחס אליו בתור נתון בטענות הלוגיות הפורמליות שאנחנו מנסחים. האמירה הזו דורשת, כמובן, כמה הבהרות רציניות, והן יגיעו, אבל לענייננו מה שחשוב פה הוא שמרגע שיש לנו את {% equation %}\mathcal{M}{% endequation %}, יש לנו בכף היד מודל של תורת הקבוצות שאפשר לשחק איתו יחסית בקלות.

הרעיון עכשיו הוא להרחיב את {% equation %}\mathcal{M}{% endequation %} בשתי דרכים שונות - פעם אחת בצורה שתניב מודל שמקיים את השערת הרצף, ופעם שניה בצורה שתניב מודל שלא מקיים את השערת הרצף. את שני אלו עושים במסגרת שיטה כללית יותר להרחבה כזו של מודלים שנקראת <strong>כפייה</strong> (Forcing). כדי להבין את הרעיון, מאוד כדאי לחשוב על דוגמא קונקרטית, שאציג בנפנוף ידיים. אמרתי שהשערת הרצף היא שמתקיים {% equation %}\left|\mathbb{R}\right|=\aleph_{1}{% endequation %}. זה אומר שצריכה להתקיים פונקציה {% equation %}f:\mathbb{R}\to\aleph_{1}{% endequation %} שהיא חח"ע ועל. עכשיו, ביקום הזעיר {% equation %}\mathcal{M}{% endequation %} שלנו פונקציה כזו לא בהכרח תהיה קיימת; אנחנו רוצים להרחיב את {% equation %}\mathcal{M}{% endequation %} בצורה ש"מכריחה" את הפונקציה להתקיים. איך עושים את זה? מסתכלים על <strong>בניות חלקיות</strong> אפשריות של {% equation %}f{% endequation %}. הרי פונקציה היא אוסף של זוגות, במקרה הנוכחי זוגות של מספר ממשי ושל איבר של {% equation %}\aleph_{1}{% endequation %}. קבוצות <strong>סופיות</strong> של זוגות כאלו בוודאי יהיו קיימות ב-{% equation %}\mathcal{M}{% endequation %}, כי אלו דברים שנבנים בקלות מאקסיומות צרמלו-פרנקל שאותן {% equation %}\mathcal{M}{% endequation %} מקיימת. 

הבעיה שהיא שפונקציות חלקיות שונות עשויות לסתור אחת את השניה. בבניה חלקית אחת של {% equation %}f{% endequation %}, המספר 0 עשוי לעבור לקלט אחד, ובבניה אחרת המספר 0 יעבור לקלט אחר; זה אומר שיש לנו שתי פונקציות חלקיות שהן "לא מתואמות". אז אנחנו נוקטים בטרמינולוגיה הבאה: לקבוצת כל הפונקציות החלקיות, {% equation %}P{% endequation %}, אנחנו קוראים בשם <strong>תנאי כפייה</strong> - התוצר של הכפייה שלנו אמור להיות פונקציה {% equation %}f:\mathbb{R}\to\aleph_{1}{% endequation %}, אז {% equation %}P{% endequation %} כוללת איברים שכל אחד מהם הוא דרישה אפשרית מה-{% equation %}f{% endequation %} הזו ("כאשר מצמצמים את {% equation %}f{% endequation %} לערכים {% equation %}0,1,2{% endequation %} מקבלים את הפלטים כך וכך"). מקבוצת תנאי הכפייה הזו אנחנו "מזקקים" תת-קבוצה {% equation %}G{% endequation %} (וויבר קורא לקבוצה כזו "אידאל גנרי" ואחרים קוראים לה "מסנן גנרי") של תנאים שכולם מסכימים אחד עם השני, ועם זאת היא גדולה מספיק כדי שרשימת הדרישות היא מציגה תהיה מאוד, מאוד מקיפה; בהינתן קבוצת תנאים שכזו, אנחנו בונים קבוצות חדשות שאנו מוסיפים ל-{% equation %}\mathcal{M}{% endequation %}, והתוצאה היא {% equation %}\mathcal{M}\left[G\right]{% endequation %} - מודל מורחב שעדיין מקיים את אקסיומות צרמלו-פרנקל, ובנוסף גם מכיל בתוכו את {% equation %}G{% endequation %}. עכשיו אפשר לבנות מתוך {% equation %}G{% endequation %} את הפונקציה המבוקשת (היא פשוט תהיה איחוד של כל הפונקציות החלקיות ב-{% equation %}G{% endequation %}). בדוגמא שלי הדרישות הוכוונו כדי להראות שהשערת הרצף נכונה; אפשר גם לתת דרישות שיראו שהשערת הרצף אינה נכונה. בשני המקרים העבודה הטכנית צריכה להיות <strong>מאוד</strong> זהירה כדי לוודא שבמעבר מ-{% equation %}\mathcal{M}{% endequation %} אל {% equation %}\mathcal{M}\left[G\right]{% endequation %} לא קילקלנו דברים. הרוב המוחץ של העבודה הטכנית שלנו יהיה מציאת הדרך הנכונה לבנות את ההרחבות כך שדברים לא יתקלקלו.

העבודה הטכנית שנדרשת לצורך כל זה אינה נוראית במיוחד - אין כאן חישובים ארוכים ומסובכים או שום דבר דומה, ההגדרות מאוד ממוקדות וההוכחות קצרות יחסית וברגע שמבינים את התמונה הגדולה הן אפילו די פשוטות. למרות זאת, רמת האבסטרקטיות של הטיעונים עשויה להיות <strong>מבלבלת מאוד</strong> לפעמים אם אין לנו דוגמא קונקרטית מול העיניים; אני מקווה שנצליח להסתדר. אני יכול להעיד על עצמי שבתחילת סדרת הפוסטים הזו הייתי מבועת לגמרי מהמחשבה על כניסה לכל הפרטים הפורמליים, ובסופו של דבר רובם נראים לי די פשוטים. אני מקווה שאלו שישרדו את סדרת הפוסטים הזו (אני לא חושב שהייתי שורד אותה, בתור קורא; אבל הייתי מדלג פחות מאשר אני מדלג בספר) ירגישו כמוני. 